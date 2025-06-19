# DRF serializer base class
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model() # Assigns CustomUser model to variable 'User'

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        # this serializer represents model 'User'
        model = User

        # Following fields are included in API response.
        fields = ['id', 'email', 'name']

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password_confirm']

    def validate(self, data):
        # validating password
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user