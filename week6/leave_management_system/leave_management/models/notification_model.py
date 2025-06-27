from django.db import models
from django.conf import settings

class Notification(models.Model):
    """
    Notification model to store alerts sent to users (mainly seniors)
    when a junior applies, updates, or deletes a leave.
    """

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_notifications',
        help_text="The user who triggered the notification",
        null=True,
        blank=True
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_notifications',
        help_text="The user who should receive the notification"
    )

    message = models.TextField(help_text="Notification message content")
    created_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False, help_text="Has the receiver read it?")

    def __str__(self):
        return f"To: {self.receiver.email} | {self.message[:50]}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
