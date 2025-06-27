from django.db import models
from django.conf import settings
from django.utils import timezone

class Leave(models.Model):
    """
    Model representing a leave request by an employee.

    Includes date range, approval status, and who approved it.
    Logic for leave count and weekends will be handled in utils.
    """

    # Leave can be one of these states
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),  # If deleted or revoked later
    ]

    # Foreign key to the employee who is requesting leave
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # Delete leave if employee is deleted
        related_name='leave_requests'  # e.g., user.leave_requests.all()
    )

    # Start and end date for the leave
    start_date = models.DateField()
    end_date = models.DateField()

    # Optional reason for leave
    reason = models.TextField(blank=True, null=True)

    # Current status of the leave
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    # Who approved/rejected this leave (a senior or admin)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_leaves'
    )

    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Set only once
    updated_at = models.DateTimeField(auto_now=True)  # Updates on each save

    def __str__(self):
        """
        Shows basic info about the leave — who requested, date range, status.
        """
        return f"{self.employee.email} - {self.start_date} to {self.end_date} ({self.status})"