from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status

from ..serializers import RegisterSerializer

class RegisterView(APIView):
    """
    Registers a new user and returns an authentication token.
    """
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'message': 'User registered successfully',
                    'token': token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Registration failed. Please fix the errors.',
                    'errors': serializer.errors
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'An error occurred during registration.',
                'error': str(e)
            }, status=status.HTTP_200_OK)


class LoginView(APIView):
    """
    Logs in a user using email and password, returns authentication token.
    """
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            if not email or not password:
                return Response({
                    "message": "Email and password are required."
                }, status=status.HTTP_200_OK)

            user = authenticate(request, email=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "message": "Login successful",
                    "token": token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": "Invalid email or password"
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "An error occurred during login.",
                "error": str(e)
            }, status=status.HTTP_200_OK)