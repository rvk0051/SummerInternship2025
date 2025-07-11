from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from ..models import ContactHR
from ..serializers import ContactHRSerializer

#View a single support request (only owner or admin can access)
class ContactHRDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = ContactHR.objects.all()
    serializer_class = ContactHRSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(user, 'is_admin', False):
            return ContactHR.objects.all()
        return ContactHR.objects.filter(user=user)

    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except ValidationError as e:
            return Response(e.detail, status=200)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as e:
            return Response(e.detail, status=200)


