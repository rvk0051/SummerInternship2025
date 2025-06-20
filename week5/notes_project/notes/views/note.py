from rest_framework import viewsets, permissions
from ..models import Note
from ..serializers import NoteSerializer
from rest_framework.response import Response

# Note ViewSet for CRUD operations
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return notes of the current user
        return Note.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):

        id = request.data.get("id")
        user = request.user
        data = request.data
        title = data.get("title")
        folder = data.get("folder")
        if Note.objects.filter(user=request.user, folder=folder, title=title).exists():
            return Response({"error": "A note with this title already exists."})

        # Manually pass the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)  # this also accepts manual ID
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            note = Note.objects.get(pk=kwargs['pk'], user=request.user)
            data = request.data
            if data.get("title") == note.title:
                return Response({"error": "The data is already up to date."}, status=200)

            # Check duplicate name
            if "title" in data:
                new_title = data["title"]
                if Note.objects.filter(user=request.user, folder=note.folder, title=new_title).exclude(id=note.id).exists():

                    return Response({"error": "A note with this name already exists."})

            # Check if all fields are same (ignore read-only)
            changed = False
            updatable_fields = ['title', 'content', 'folder']

            for field in updatable_fields:
                if field in data:
                    new_value = data.get(field)
                    old_value = getattr(note, field)
                    if str(new_value) != str(old_value):  # Comparing old and new values
                        changed = True
                        break

            if not changed:
                return Response({"error": "No changes detected. The data is already up to date."}, status=200)

            # updating the folder
            serializer = self.get_serializer(note, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except Note.DoesNotExist:
            return Response({"error": "Note does not exist."})

    def destroy(self, request, *args, **kwargs):
        # function for deleting the note.
        try:
            # Only try to fetch notes belonging to current user
            note = Note.objects.get(pk=kwargs['pk'], user=request.user)
            note.delete()
            return Response({"error": "Note deleted successfully."})

        # if folder doesn't exist, handle exception.
        except Note.DoesNotExist:
            # Either ID doesn't exist or it's not current user's note
            return Response({"error": "Note does not exist."})

