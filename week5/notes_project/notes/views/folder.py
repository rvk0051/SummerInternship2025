from rest_framework import viewsets, permissions
from ..models import Folder
from ..serializers import FolderSerializer
from rest_framework.response import Response

# Folder ViewSet for CRUD operations
class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return folders of the current user
        return Folder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        # When listing, only show top-level folders (parent=None)
        queryset = self.get_queryset().filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)