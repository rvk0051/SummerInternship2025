# authentication/views/user_views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers.user_serializers import UserSerializer, JuniorSerializer

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):  # user will get it's own data
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class JuniorUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):  # get juniors data
        juniors = request.user.juniors.all()
        if juniors.exists():
            serializer = JuniorSerializer(juniors, many=True)
            return Response(serializer.data)
        return Response({"message": "No juniors under you."})
