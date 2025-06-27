'''
This file is required so that every month's first date present month's leave and next month's leave gets updated automatically updated.
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leave_management_system.settings")
django.setup()

from leave_management.utils import carry_forward_leaves

carry_forward_leaves()
