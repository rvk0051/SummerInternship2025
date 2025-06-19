from rest_framework.views import APIView  # Base class for DRF views (non-viewset)
from rest_framework.response import Response  # To return API responses
from rest_framework import status  # For readable HTTP status codes
from .serializers import RegisterSerializer, UserSerializer  # Serializers for user creation and display
from django.contrib.auth import authenticate  # Auth method to verify user credentials
from rest_framework.authtoken.models import Token  # Token model for token-based authentication

# View for registering new users
class RegisterView(APIView):

    def post(self, request):
        # Deserialize the incoming JSON data using RegisterSerializer
        serializer = RegisterSerializer(data=request.data)

        # If the provided data is valid (email, password, etc.)
        if serializer.is_valid():
            # Save the user to the database
            user = serializer.save()

            # Generate a token for this user (or fetch existing one)
            token, _ = Token.objects.get_or_create(user=user)

            # Return user data and token in response
            return Response({
                "user": UserSerializer(user).data,  # Nested serializer to send back user info
                "token": token.key  # Auth token sent to client
            }, status=status.HTTP_201_CREATED)

        # If validation fails, return error messages
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for logging in users using email and password
class LoginView(APIView):

    def post(self, request):
        # Extract email and password from the request body
        email = request.data.get("email")
        password = request.data.get("password")

        # Use custom authentication that accepts email (not username)
        user = authenticate(request, email=email, password=password)

        # If user credentials are correct
        if user:
            # Fetch or create a token for this user
            token, _ = Token.objects.get_or_create(user=user)

            # Send back user info and token
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            })

        # If authentication fails, send error response
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
