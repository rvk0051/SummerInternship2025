from rest_framework import serializers
from .models import Attendance
from datetime import time

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model.
    """

    class Meta:
        model = Attendance
        fields = [
            'id',
            'employee',
            'date',
            'check_in',
            'check_out',
            'total_hours',
            'status'
        ]
        read_only_fields = ['total_hours', 'status', 'employee']

    def validate(self, data):
        check_in = data.get('check_in') or self.instance.check_in if self.instance else None
        check_out = data.get('check_out') or self.instance.check_out if self.instance else None

        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError({
                "message": "Check-out must be after check-in."
            })

        return data

    def create(self, validated_data):
        validated_data['employee'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
