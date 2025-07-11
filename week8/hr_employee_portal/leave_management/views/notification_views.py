from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..models import Notification
from ..serializers import NotificationSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet to handle notifications:
    - List all notifications of logged-in user.
    - Mark as read (custom action).
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(receiver=self.request.user).order_by('-created_at')

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        """
        Mark a single notification as read.
        """
        try:
            notification = self.get_object()
            if notification.receiver != request.user:
                return Response({'message': 'Not authorized to mark this notification.'}, status=200)

            notification.is_read = True
            notification.save()
            return Response({'message': 'Notification marked as read.'}, status=200)

        except Exception as e:
            return (Response({'message': f'Failed to mark as read: {str(e)}'}, status=200)

    @action(detail=False, methods=['post'], url_path='mark-all-read'))
    def mark_all_read(self, request):
        """
        Mark all unread notifications of the logged-in user as read.
        """
        try:
            updated_count = Notification.objects.filter(
                receiver=request.user, is_read=False
            ).update(is_read=True)
            return Response({
                "message": f"{updated_count} notification(s) marked as read."
            }, status=200)

        except Exception as e:
            return Response({
                "message": f"Failed to mark all as read: {str(e)}"
            }, status=200)
