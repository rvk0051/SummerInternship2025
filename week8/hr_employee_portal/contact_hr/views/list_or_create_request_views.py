from rest_framework import generics, permissions
from rest_framework.response import Response
from ..models import ContactHR
from ..serializers import ContactHRSerializer

# List all support requests and allow creating a new one
class ContactHRListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ContactHRSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(user, 'is_admin', False):
            return ContactHR.objects.all()  # Admin can see all
        return ContactHR.objects.filter(user=user)  # Users see only their own

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=200)

