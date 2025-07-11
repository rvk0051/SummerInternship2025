from rest_framework import serializers, status
from datetime import date
from ..models import Leave
from ..utils import get_working_days_in_leave


class LeaveSerializer(serializers.ModelSerializer):
    """
    Validates leave data:
    - No past dates
    - Start ≤ End
    - Can't edit passed dates
    - 4 days leave/month
    - Show employee email instead of ID
    """

    employee = serializers.EmailField(source='employee.email', read_only=True)

    class Meta:
        model = Leave
        fields = '__all__'
        read_only_fields = ['employee', 'status', 'created_at']

    def validate(self, data):
        try:
            request = self.context.get('request')
            user = request.user if request else None

            if not user:
                raise serializers.ValidationError({"message": "User not authenticated."})

            today = date.today()
            is_update = self.instance is not None

            # Handle dates
            start = data.get('start_date', self.instance.start_date if is_update else None)
            end = data.get('end_date', self.instance.end_date if is_update else None)

            # Optional half-day flags (default to False if not provided)
            is_start_half_day = data.get("is_start_half_day", False)
            is_end_half_day = data.get("is_end_half_day", False)

            # Required field checks
            if not start or not end:
                raise serializers.ValidationError({"message": "Both start_date and end_date are required."})

            # Date order check
            if start > end:
                raise serializers.ValidationError({"message": "Start date should be earlier than end date."})

            # Overlapping leaves check
            overlaps = Leave.objects.filter(
                employee=user,
                start_date__lte=end,
                end_date__gte=start
            ).exclude(pk=self.instance.pk if is_update else None)

            if overlaps.exists():
                raise serializers.ValidationError({"message": "You already have a leave in this range."})

            # Past start date not allowed on creation
            if not is_update and start < today:
                raise serializers.ValidationError({"message": "Start date cannot be in the past."})

            # Working days calculation (taking half-days into account)
            existing_leaves = Leave.objects.filter(
                employee=user,
                status__in=['approved', 'pending']
            ).exclude(pk=self.instance.pk if is_update else None)

            used_days = 0
            for leave in existing_leaves:
                days, _ = get_working_days_in_leave(leave.start_date, leave.end_date, leave.is_start_half_day, leave.is_end_half_day)
                used_days += days

            current_days, _ = get_working_days_in_leave(start, end, is_start_half_day, is_end_half_day)

            if used_days + current_days > 4:
                raise serializers.ValidationError({"message": "Monthly leave limit exceeded (max 4 working days)."})

            # Special update rules
            if is_update:
                if 'start_date' in data:
                    if self.instance.start_date <= today:
                        raise serializers.ValidationError({"message": "Start date can't be changed after it begins."})
                    if start < today:
                        raise serializers.ValidationError({"message": "New start date cannot be in the past."})

                if 'end_date' in data:
                    if self.instance.end_date <= today:
                        raise serializers.ValidationError({"message": "End date can't be changed after it ends."})
                    if end < today:
                        raise serializers.ValidationError({"message": "New end date cannot be in the past."})

            return data

        except serializers.ValidationError:
            raise
        except Exception as e:
            raise serializers.ValidationError({"message": f"Validation failed: {str(e)}"})

    def create(self, validated_data):
        try:
            validated_data['employee'] = self.context['request'].user
            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError({"message": f"Leave creation failed: {str(e)}"})

    def update(self, instance, validated_data):
        try:
            instance.status = 'PENDING'  # Reset to pending if updated
            return super().update(instance, validated_data)
        except Exception as e:
            raise serializers.ValidationError({"message": f"Leave update failed: {str(e)}"})