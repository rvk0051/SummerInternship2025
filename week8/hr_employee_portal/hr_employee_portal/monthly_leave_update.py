'''
This file is required so that every month's first date, present month's leave and next month's leave gets updated automatically updated and helps keep attendance on track
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leave_management_system.settings")
django.setup()

from leave_management.utils import carry_forward_leaves
from ..attendance_system.utils import reset_monthly_attendance_counts

carry_forward_leaves()
reset_monthly_attendance_counts()