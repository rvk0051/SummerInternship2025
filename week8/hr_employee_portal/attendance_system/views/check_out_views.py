from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Attendance
from ..serializers import AttendanceSerializer


class CheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            today = timezone.localdate()

            try:
                attendance = Attendance.objects.get(employee=user, date=today)
            except Attendance.DoesNotExist:
                return Response({
                    "message": "Check-in required before check-out."
                }, status=200)

            if attendance.check_out:
                return Response({
                    "message": "Already checked out for today."
                }, status=200)

            now = timezone.now()
            check_out_time = now.time()

            attendance.check_out = check_out_time
            attendance.save()  # status and total_hours updated automatically

            return Response({
                "message": "Check-out successful.",
                "data": AttendanceSerializer(attendance).data
            }, status=200)

        except Exception as e:
            return Response({
                "message": f"Check-out failed: {str(e)}"
            }, status=200)

