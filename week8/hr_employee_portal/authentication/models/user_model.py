import calendar
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Q, When, Case
from decimal import Decimal
from leave_management.utils import get_working_days_in_leave

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True, null=True, default='')
    email = models.EmailField(_('email address'), unique=True)

    is_admin = models.BooleanField(default=False)

    senior = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='juniors'
    )

    leaves_available_this_month = models.DecimalField(max_digits=2, decimal_places=1, default=4, validators=[MinValueValidator(0)])
    leaves_available_next_month = models.DecimalField(max_digits=2, decimal_places=1, default=4, validators=[MinValueValidator(0)])
    total_present_days = models.DecimalField(
        max_digits=4, decimal_places=1,
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(31)]
    )

    total_absent_days = models.DecimalField(
        max_digits=4, decimal_places=1,
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(31)]
    )

    total_working_days_in_this_month = models.DecimalField(
        max_digits=4, decimal_places=1,
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(31)]
    )

    total_leave_days_in_this_month = models.DecimalField(
        max_digits=4, decimal_places=1,
        default=Decimal('0.0'),
        validators=[MinValueValidator(0), MaxValueValidator(31)]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.senior and not self.is_admin:
            try:
                admin_user = User.objects.filter(is_admin=True).first()
                if admin_user:
                    self.senior = admin_user
            except:
                pass
        super().save(*args, **kwargs)

    @property
    def today_attendance_status(self):
        today_attendance = self.attendances.filter(date=date.today()).first()
        # returning attendance status
        return today_attendance.status if today_attendance else "NOT_MARKED"

    @property
    def total_present_days_in_this_month(self):
        today = timezone.now()
        return self.attendances.filter(
            date__year=today.year,
            date__month=today.month
        ).aggregate(
            total=Sum(
                ExpressionWrapper(
                    Case(
                        When(status='FULL_DAY', then=1.0),
                        When(status='HALF_DAY', then=0.5),
                        default=0.0,
                        output_field=DecimalField()
                    ), output_field=DecimalField()
                )
            )
        )['total'] or 0.0

    @property
    def total_absent_days_in_this_month(self):
        today = timezone.now()
        return self.attendances.filter(
            date__year=today.year,
            date__month=today.month,
            status='ABSENT'
        ).count()


    @property
    def total_working_days_in_this_month(self):
        today = date.today()
        year = today.year
        month = today.month
        _, last_day = calendar.monthrange(year, month)
        working_days = 0
        for day in range(1, last_day + 1):
            weekday = date(year, month, day).weekday()
            if weekday < 5:
                working_days += 1
        return working_days
