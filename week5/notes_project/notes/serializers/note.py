from rest_framework import serializers
from ..models import Note

class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model.
    Handles serialization (convert to JSON) and deserialization (validate incoming data).
    """

    class Meta:
        model = Note  # Link this serializer to the Note model

        # These are the fields included in API input/output
        fields = ['id', 'title', 'content', 'folder', 'user', 'created_at', 'updated_at']

        # These fields are automatically handled by the backend and should not be editable by the user
        read_only_fields = ['user', 'created_at', 'updated_at']


    def update(self, instance, validated_data):
        """
        Called when updating an existing note.
        Allows updating title, content, and optionally folder.
        Does not allow changing the user.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.folder = validated_data.get('folder', instance.folder)
        instance.save()
        return instance

