# blogging/signals.py

"""
Automatically creates a Profile instance whenever a new User is created.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile for every new User.
    """
    if created:
        Profile.objects.create(user=instance)
