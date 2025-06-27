from rest_framework import serializers
from ..models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Notification objects.
    Includes sender and receiver emails, message, timestamp, and read status.
    """

    sender_email = serializers.EmailField(source='sender.email', read_only=True)
    receiver_email = serializers.EmailField(source='receiver.email', read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'sender_email',
            'receiver_email',
            'message',
            'created_at',
            'is_read'
        ]
        read_only_fields = [
            'sender_email',
            'receiver_email',
            'created_at'
        ]

