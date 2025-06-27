from datetime import timedelta
from datetime import date
from django.contrib.auth import get_user_model

def get_working_days_in_leave(start_date, end_date):
    '''
    It return the no. of days, the leave is to be taken.
    '''
    total_days = 0
    current = start_date

    while current <= end_date:
        if current.weekday() not in (5, 6):  # 5 = Saturday, 6 = Sunday
            total_days += 1
        current += timedelta(days=1)

    return total_days

User = get_user_model()

def carry_forward_leaves():
    '''
    If the leaves are not used in a month, those are carry forwarded to the the next month.
    '''
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
    leave_days = get_working_days_in_leave(leave.start_date, leave.end_date)

    if leave.start_date.month == today.month:
        user.leaves_available_this_month += leave_days

    elif leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month += leave_days

    user.save()

def update_user_leaves_on_update(old_leave, new_leave):
    user = old_leave.employee
    today = date.today()

    # Restore old leave days
    old_days = get_working_days_in_leave(old_leave.start_date, old_leave.end_date)

    if old_leave.start_date.month == today.month:
        user.leaves_available_this_month += old_days

    elif old_leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month += old_days

    # Subtract new leave days
    new_days = get_working_days_in_leave(new_leave.start_date, new_leave.end_date)

    if new_leave.start_date.month == today.month:
        user.leaves_available_this_month -= new_days

    elif new_leave.start_date.month == (today.month + 1) % 12:
        user.leaves_available_next_month -= new_days

    user.save()