from rest_framework import serializers
from ..models import Folder, Note

class FolderNotePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title']  # Only showing id and title of notes

class FolderSerializer(serializers.ModelSerializer):
    # Creates a serializer for the Folder model
    id = serializers.IntegerField(required=False)

    subfolders = serializers.SerializerMethodField() # Adds a custom field to return nested children folders

    notes = serializers.SerializerMethodField()  # custom field for embedded notes

    class Meta:

        # This serializer represents 'Folder' model.
        model = Folder

        # following fields are to be serialized (converted to JSON).
        fields = ['id', 'name', 'parent', 'user', 'created_at', 'subfolders', 'notes']

        # 	These fields can't be edited directly by the user
        read_only_fields = ['user', 'created_at']

    def get_subfolders(self, obj):
        # Automatically called to populate the 'subfolders' field.
        # This returns all direct child folders of this folder (recursive structure).

        return FolderSerializer(obj.subfolders.all(), many=True).data

    def get_notes(self, obj):
        # Gets all notes inside this folder
        notes = Note.objects.filter(folder=obj)
        return FolderNotePreviewSerializer(notes, many=True).data

    def validate(self, data):
        user = self.context['request'].user
        name = data.get('name')
        parent = data.get('parent')

        return data