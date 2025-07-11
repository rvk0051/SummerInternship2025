from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'check_in', 'check_out', 'status', 'total_hours']
    list_filter = ['date', 'status', 'employee']
    search_fields = ['employee__email']
    ordering = ['-date']
