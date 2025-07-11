from rest_framework import serializers
from ..models import User
from attendance_system.models import Attendance
from attendance_system.utils import get_working_days_in_current_month
from leave_management.models import Leave
from datetime import date
from django.db.models import Sum, Case, When, DecimalField, ExpressionWrapper
from decimal import Decimal
class UserSerializer(serializers.ModelSerializer):
    total_present_days_in_this_month = serializers.SerializerMethodField()
    total_absent_days_in_this_month = serializers.SerializerMethodField()
    total_working_days_in_this_month = serializers.SerializerMethodField()
    total_leave_days_in_this_month = serializers.SerializerMethodField()
    senior_email = serializers.SerializerMethodField()
    today_attendance_status = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_admin', 'is_staff', 'is_superuser',
            'senior_email',
            'today_attendance_status',
            'leaves_available_this_month', 'leaves_available_next_month',
            'total_leave_days_in_this_month',
            'total_working_days_in_this_month',
            'total_present_days_in_this_month', 'total_absent_days_in_this_month'
        ]
        read_only_fields = fields

    def get_total_present_days_in_this_month(self, obj):
        today = date.today()
        result = Attendance.objects.filter(
            employee=obj,
            date__month=today.month,
            date__year=today.year
        ).aggregate(
            total=Sum(
                Case(
                    When(status='FULL_DAY', then=1.0),
                    When(status='HALF_DAY', then=0.5),
                    default=0.0,
                    output_field=DecimalField()
                )
            )
        )
        return result['total'] or 0.0

    def get_total_absent_days_in_this_month(self, obj):
        today = date.today()
        count_absent_days = Attendance.objects.filter(
            employee=obj,
            date__month=today.month,
            date__year=today.year,
            status='ABSENT'
        ).count()
        return Decimal(count_absent_days) or 0.0

    def get_total_leave_days_in_this_month(self, obj):
        today = date.today()
        leaves = Leave.objects.filter(
            employee=obj,
            status='APPROVED',
            start_date__lte=today.replace(day=31),
            end_date__gte=today.replace(day=1)
        )

        total = 0.0
        for leave in leaves:
            start = max(leave.start_date, today.replace(day=1))
            end = min(leave.end_date, today.replace(day=31))
            days = (end - start).days + 1.0
            if getattr(leave, 'is_half_day', False):
                total += 0.5
            else:
                total += days
        return total

    def get_total_working_days_in_this_month(self, obj):
        return get_working_days_in_current_month()

    def get_senior_email(self, obj):
        return obj.senior.email if obj.senior else None


class JuniorSerializer(serializers.ModelSerializer):
    # Used for junior's info.
    juniors = serializers.SerializerMethodField()
    senior_email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'is_staff', 'is_superuser', 'senior_email', 'leaves_available_this_month', 'leaves_available_next_month','total_present_days','total_absent_days', 'juniors']

    def get_senior_email(self, obj):
        '''
        function for getting senior's email.
        '''
        return obj.senior.email if obj.senior else None

    def get_juniors(self, obj):
        '''
        function to get junior's info.
        '''
        juniors = obj.juniors.all()
        if juniors.exists():
            return JuniorSerializer(juniors, many=True).data
        return "No juniors"
