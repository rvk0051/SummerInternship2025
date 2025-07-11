from datetime import timedelta
from datetime import date
from django.contrib.auth import get_user_model
from datetime import timedelta
from decimal import Decimal

def get_working_days_in_leave(start_date, end_date, is_start_half_day=False, is_end_half_day=False):
    """
    Returns:
    - working_days: Total leave days (float)
    - holidays: List of weekends (Saturday/Sunday)
    """
    total_days = 0.0
    holidays = []
    current = start_date

    # Single-day leave case
    if start_date == end_date:
        if start_date.weekday() in (5, 6):  # Sat/Sun
            holidays.append(start_date)
            return 0.0, holidays
        if is_start_half_day or is_end_half_day:
            return 0.5, holidays
        return 1.0, holidays

    while current <= end_date:
        if current.weekday() in (5, 6):
            holidays.append(current)
        else:
            total_days += 1.0
        current += timedelta(days=1)

    # Adjust for half-days only if it's not a single-day leave
    if is_start_half_day and start_date.weekday() not in (5, 6):
        total_days -= 0.5

    if is_end_half_day and end_date.weekday() not in (5, 6):
        total_days -= 0.5

    return total_days, holidays

def carry_forward_leaves():
    '''
    If the leaves are not used in a month, those are carry forwarded to the the next month.
    '''
    User = get_user_model()
    today = date.today()
    if today.day != 1:
        return  # Only proceed on 1st day of the month

    for user in User.objects.all():
        unused = user.leaves_this_month
        user.leaves_available_this_month = user.leaves_available_next_month + unused
        user.leaves_available_next_month = 4
        user.save()


def adjust_user_leaves_on_cancel(leave):
    '''
    when a user cancels a leave, the leaves should be adjusted.
    '''
    user = leave.employee
    today = date.today()

    leave_days, _ = get_working_days_in_leave(leave.start_date, leave.end_date,
                                              getattr(leave, 'is_start_half_day', False),
                                              getattr(leave, 'is_end_half_day', False))

    if leave.start_date.month == today.month:
        user.leaves_available_this_month += Decimal(f"{leave_days}")

    elif leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month += Decimal(f"{leave_days}")

    user.save()


def update_user_leaves_on_update(old_leave, new_leave):
    user = old_leave.employee
    today = date.today()

    old_days, _ = get_working_days_in_leave(old_leave.start_date, old_leave.end_date,
                                            getattr(old_leave, 'is_start_half_day', False),
                                            getattr(old_leave, 'is_end_half_day', False))

    new_days, _ = get_working_days_in_leave(new_leave.start_date, new_leave.end_date,
                                            getattr(new_leave, 'is_start_half_day', False),
                                            getattr(new_leave, 'is_end_half_day', False))

    if old_leave.start_date.month == today.month:
        user.leaves_available_this_month += Decimal(f"{old_days}")
    elif old_leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month += Decimal(f"{old_days}")

    if new_leave.start_date.month == today.month:
        user.leaves_available_this_month -= Decimal(f"{new_days}")
    elif new_leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month -= Decimal(f"{new_days}")

    user.save()

