from datetime import timedelta

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