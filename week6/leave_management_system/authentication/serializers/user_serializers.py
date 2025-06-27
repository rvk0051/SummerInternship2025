# authentication/serializers/user_serializers.py
from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    senior_email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'is_staff', 'is_superuser', 'senior_email']

    def get_senior_email(self, obj):
        return obj.senior.email if obj.senior else None

class JuniorSerializer(serializers.ModelSerializer):
    juniors = serializers.SerializerMethodField()
    senior_email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'is_staff', 'is_superuser', 'senior_email', 'juniors']

    def get_senior_email(self, obj):
        return obj.senior.email if obj.senior else None

    def get_juniors(self, obj):
        juniors = obj.juniors.all()
        if juniors.exists():
            return JuniorSerializer(juniors, many=True).data
        return "No juniors"
