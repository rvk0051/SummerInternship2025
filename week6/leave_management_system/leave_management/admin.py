from django.contrib import admin
from .models import Leave, Notification

# registering 'Leave' model with the default admin interface
admin.site.register(Leave)

# registering model 'Notification' using decorator so that we could customize it.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'created_at', 'is_read')
    search_fields = ('sender_email', 'receiver_email', 'message')
    list_filter = ('is_read', 'created_at')