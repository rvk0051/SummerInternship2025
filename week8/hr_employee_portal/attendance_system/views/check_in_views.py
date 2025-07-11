from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Attendance
from ..serializers import AttendanceSerializer

class CheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            today = timezone.localdate()

            if Attendance.objects.filter(employee=user, date=today).exists():
                return Response({
                    "message": "Already checked in for today."
                }, status=200)

            now = timezone.now()
            check_in_time = now.time()

            attendance = Attendance.objects.create(
                employee=user,
                date=today,
                check_in=check_in_time
            )

            return Response({
                "message": "Check-in successful.",
                "data": AttendanceSerializer(attendance).data
            }, status=200)

        except Exception as e:
            return Response({
                "message": f"Check-in failed: {str(e)}"
            }, status=200)
