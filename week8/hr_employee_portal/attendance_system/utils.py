from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, date, time
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import calendar

from leave_management.models import Leave
from attendance_system.models import Attendance

User = get_user_model()

def calculate_total_hours(check_in, check_out):
    """
    Calculates the total hours between check-in and check-out.
    Returns 0.0 if any input is missing or invalid.
    """
    try:
        if not check_in or not check_out:
            return 0.0

        dt_in = datetime.combine(date.today(), check_in)
        dt_out = datetime.combine(date.today(), check_out)

        if dt_out <= dt_in:
            return 0.0  # Invalid range

        delta = dt_out - dt_in
        return round(delta.total_seconds() / 3600, 2)
    except Exception:
        return 0.0


def get_working_days_in_current_month():
    """
    Returns total working days (Mon–Fri) in the current month.
    Weekends (Sat, Sun) are excluded.
    """
    try:
        today = date.today()
        year = today.year
        month = today.month
        _, last_day = calendar.monthrange(year, month)

        working_days = sum(
            1 for day in range(1, last_day + 1)
            if date(year, month, day).weekday() < 5
        )
        return working_days
    except Exception as e:
        print(f"Error calculating working days: {e}")
        return 0


def is_weekend(check_date):
    return check_date.weekday() >= 5


def deduct_leave_or_count_absent(user, attendance_obj, worked_hours):
    """
    Adjusts leave or marks absent based on remaining leave and worked hours.
    Should be called inside model save or batch update.
    """
    if is_weekend(attendance_obj.date):
        attendance_obj.status = 'WEEKEND'
        return

    if worked_hours >= 7:
        attendance_obj.status = 'PRESENT'
    elif 4 <= worked_hours < 7:
        if user.leaves_available_this_month >= 0.5:
            user.leaves_available_this_month -= 0.5
            attendance_obj.status = 'HALF_DAY'
            create_auto_leave(user, attendance_obj.date, is_half=True)
        else:
            attendance_obj.status = 'ABSENT'
            user.total_absent_days = (user.total_absent_days or 0) + 0.5
    elif worked_hours < 4:
        if user.leaves_available_this_month >= 1:
            user.leaves_available_this_month -= 1
            attendance_obj.status = 'ON_LEAVE'
            create_auto_leave(user, attendance_obj.date)
        else:
            attendance_obj.status = 'ABSENT'
            user.total_absent_days = (user.total_absent_days or 0) + 1

    user.save()
    attendance_obj.save()


def create_auto_leave(user, leave_date, is_half=False):
    """
    Automatically creates a leave entry for the day (used during late/absent adjustment).
    """
    Leave.objects.create(
        employee=user,
        start_date=leave_date,
        end_date=leave_date,
        status='PENDING',
        reason='Auto-marked due to insufficient attendance',
        is_half_day=is_half
    )


def auto_update_previous_day_attendance():
    """
    Should be scheduled to run every day after 2 PM.
    For any previous day's check-in without check-out, finalize status.
    """
    previous_day = date.today() - timedelta(days=1)
    all_attendances = Attendance.objects.filter(date=previous_day)

    for record in all_attendances:
        if not record.check_out:
            # If only check-in, still mark working based on current data
            record.status = 'PRESENT'
        else:
            worked_hours = calculate_total_hours(record.check_in, record.check_out)
            deduct_leave_or_count_absent(record.employee, record, worked_hours)
