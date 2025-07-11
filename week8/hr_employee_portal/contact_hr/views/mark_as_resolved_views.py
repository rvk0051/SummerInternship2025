from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from ..models import ContactHR
from ..serializers import ContactHRSerializer

class MarkAsResolvedAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        try:
            contacthr = ContactHR.objects.get(pk=pk)

            if contacthr.status == 'Resolved':
                return Response({"message": "Already marked as Resolved."}, status=200)

            contacthr.status = 'Resolved'
            contacthr.save()
            return Response({"message": "Marked as Resolved successfully."}, status=200)

        except ContactHR.DoesNotExist:
            return Response({"message": "request not found."}, status=200)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=200)