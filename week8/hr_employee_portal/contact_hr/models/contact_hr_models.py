from django.db import models
from django.conf import settings

class ContactHR(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.title} - {self.user.email}"
