from rest_framework import serializers
from ..models import ContactHR

class ContactHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHR
        fields = '__all__'  # Includes all fields from the model
        read_only_fields = ['user', 'created_at', 'updated_at', 'status']  # User set from request; status updated by HR only

    def validate(self, attrs):
        """
        Prevent user from manually submitting read-only fields.
        """
        read_only = set(self.Meta.read_only_fields)
        passed_fields = set(self.initial_data.keys())
        invalid_fields = read_only.intersection(passed_fields)

        if invalid_fields:
            raise serializers.ValidationError({
                "message": f"You are not allowed to set read-only fields: {', '.join(invalid_fields)}"
            })

        return super().validate(attrs)

    def create(self, validated_data):
        try:
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError({
                "message": f"Failed to submit query: {str(e)}"
            })

    def update(self, instance, validated_data):
        if instance.status == 'Resolved':
            raise serializers.ValidationError({"message": "You cannot update a resolved request."}, code=200)
        return super().update(instance, validated_data)