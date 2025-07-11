from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, time

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('FULL_DAY', 'Full Day'),
        ('HALF_DAY', 'Half Day'),
        ('ABSENT', 'Absent'),
        ('ON_LEAVE', 'On Leave'),
        ('WEEKEND', 'Weekend'),
    ]

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    date = models.DateField(default=timezone.localdate)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ABSENT')
    total_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.email} - {self.date} - {self.status}"

    def save(self, *args, **kwargs):
        # Don't allow save for future dates
        if self.date > timezone.localdate():
            return

        now_time = timezone.now().time()
        after_2_pm = now_time > time(14, 0)

        # WEEKEND short-circuit (if no check-in)
        if self.date.weekday() >= 5 and not self.check_in and not self.check_out:
            self.status = 'WEEKEND'
            super().save(*args, **kwargs)
            return

        # If check-in and check-out present → calculate
        if self.check_in and self.check_out:
            dt_in = datetime.combine(self.date, self.check_in)
            dt_out = datetime.combine(self.date, self.check_out)

            duration = dt_out - dt_in
            hours = duration.total_seconds() / 3600
            self.total_hours = round(hours, 2)

            if self.total_hours >= 7:
                self.status = 'FULL_DAY'
            elif self.total_hours >= 4:
                self.status = 'HALF_DAY'
            else:
                if after_2_pm:
                    if self.employee.leaves_available_this_month >= 1:
                        self.status = 'ON_LEAVE'
                        self.employee.leaves_available_this_month -= 1
                    elif self.employee.leaves_available_this_month >= 0.5:
                        self.status = 'HALF_DAY'
                        self.employee.leaves_available_this_month -= 0.5
                    else:
                        self.status = 'ABSENT'
                        self.employee.total_absent_days = (self.employee.total_absent_days or 0) + 1

        elif self.check_in and not self.check_out:
            # Only check-in done
            self.status = 'PRESENT'

        elif not self.check_in:
            if after_2_pm:
                if self.employee.leaves_available_this_month >= 1:
                    self.status = 'ON_LEAVE'
                    self.employee.leaves_available_this_month -= 1
                else:
                    self.status = 'ABSENT'
                    self.employee.total_absent_days = (self.employee.total_absent_days or 0) + 1

        super().save(*args, **kwargs)
        self.employee.save()
