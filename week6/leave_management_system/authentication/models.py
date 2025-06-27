from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

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

    leaves_available_this_month = models.PositiveIntegerField(default=4)
    leaves_available_next_month = models.PositiveIntegerField(default=4)

    USERNAME_FIELD = 'email'  # Login using email
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.senior and not self.is_admin:
            try:
                admin_user = User.objects.filter(is_admin=True).first()
                if admin_user:
                    self.senior = admin_user
            except:
                pass  # Handles case where no admin exists yet
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} (Senior: {self.senior.email if self.senior else 'None'})"