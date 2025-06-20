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

    def create(self, request, *args, **kwargs):
        id = request.data.get("id")
        user = request.user
        data = request.data
        name = data.get("name")
        parent = data.get("parent")
        if Folder.objects.filter(user=request.user, parent=parent, name=name).exists():
            return Response({"error": "A folder with this title already exists in the parent folder you requested."})

        # Manually pass the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)  # this also accepts manual ID
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=kwargs['pk'], user=request.user)
            data = request.data
            if data.get("name") == folder.name:
                return Response({"error": "The data is already up to date."}, status=200)

            # Check duplicate name
            if "name" in data:
                new_name = data["name"]
                if Folder.objects.filter(user=request.user, parent=folder.parent, name=new_name).exclude(
                        id=folder.id).exists():

                    return Response({"error": "A folder with this name already exists."})

            # Check if all fields are same (ignore read-only)
            changed = False
            updatable_fields = ['name', 'description', 'parent']  # include any other you allow update

            for field in updatable_fields:
                if field in data:
                    new_value = data.get(field)
                    old_value = getattr(folder, field)
                    if str(new_value) != str(old_value):  # Convert both to string to handle comparison
                        changed = True
                        break

            if not changed:
                return Response({"error": "The data is already up to date."}, status=200)

            # Proceed with actual update
            serializer = self.get_serializer(folder, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Folder.DoesNotExist:
            return Response({"error": "Folder does not exist."})

    def destroy(self, request, *args, **kwargs):
        # function for deleting folder
        try:
            folder = Folder.objects.get(pk=kwargs['pk'], user=request.user)
            folder.delete()
            return Response({"error": "Folder deleted successfully."})

        # if folder doesn't exist, handle exception.
        except Folder.DoesNotExist:
            return Response({"error": "Folder does not exist."})
