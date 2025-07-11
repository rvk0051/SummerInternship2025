from django.utils.dateparse import parse_date
from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Attendance
from ..serializers import AttendanceSerializer
from authentication.models import User

class AttendanceByDateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            query_date_str = request.query_params.get('date')
            employee_id = request.query_params.get('employee_id')

            if not query_date_str:
                return Response({"message": "Date query parameter is required."}, status=200)

            query_date = parse_date(query_date_str)
            if not query_date:
                return Response({"message": "Invalid date format. Use YYYY-MM-DD."}, status=200)

            if query_date > date.today():
                return Response({"message": "Cannot fetch attendance for a future date."}, status=200)

            target_user = user
            if employee_id:
                try:
                    target_user = User.objects.get(id=employee_id)
                    if not (user == target_user or target_user.senior == user or user.is_admin):
                        return Response({"message": "You do not have permission to view this attendance."}, status=200)
                except User.DoesNotExist:
                    return Response({"message": "Employee not found."}, status=200)

            try:
                attendance = Attendance.objects.get(employee=target_user, date=query_date)
                serializer = AttendanceSerializer(attendance)
                return Response({"data": serializer.data}, status=200)

            except Attendance.DoesNotExist:
                return Response({"message": "No attendance found for the given date."}, status=200)

        except Exception as e:
            return Response({"message": f"Error occurred: {str(e)}"}, status=200)
