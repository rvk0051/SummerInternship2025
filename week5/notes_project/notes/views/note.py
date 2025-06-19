from rest_framework import viewsets, permissions
from ..models import Note
from ..serializers import NoteSerializer

# Note ViewSet for CRUD operations
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return notes of the current user
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)
