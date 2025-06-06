# blogging/apps.py

"""
App configuration for the blogging app.
Connects signals on app ready.
"""

from django.apps import AppConfig

class BloggingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogging'

    def ready(self):
        """
        Import signal handlers when the app is ready.
        """
        from . import signals # Ensures user profile is created automatically
