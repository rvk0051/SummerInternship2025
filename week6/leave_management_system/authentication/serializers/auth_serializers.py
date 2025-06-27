from rest_framework import serializers
from ..models import User

class RegisterSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)
    senior_email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'new_password', 'confirm_new_password', "senior_email", "username"]

    def validate(self, data):
        """
        Ensure both password fields match and 'id' is not provided manually.
        All exceptions handled with try-except and return status 200-compatible messages.
        """
        try:
            if 'id' in self.initial_data:
                raise Exception("User is not allowed to set 'id' manually.")

            if data['new_password'] != data['confirm_new_password']:
                raise Exception("Passwords do not match.")
        except Exception as e:
            raise serializers.ValidationError({
                "message": str(e)
            })

        return data

    def create(self, validated_data):
        try:
            senior_email = validated_data.pop('senior_email', None)
            validated_data.pop('confirm_new_password')
            password = validated_data.pop('new_password')

            user = User(**validated_data)
            user.set_password(password)

            if senior_email:
                senior_user = User.objects.filter(email=senior_email).first()
                if not senior_user:
                    raise serializers.ValidationError({
                        "senior_email": "No user with this email exists."
                    })
                user.senior = senior_user

            user.save()
            return user

        except serializers.ValidationError:
            raise

        except Exception as e:
            raise serializers.ValidationError({
                "message": f"User creation failed: {str(e)}"
            })