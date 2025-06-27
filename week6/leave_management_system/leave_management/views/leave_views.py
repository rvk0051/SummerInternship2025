from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from ..models import Leave, Notification
from ..serializers import LeaveSerializer
from ..utils import adjust_user_leaves_on_cancel, update_user_leaves_on_update, get_working_days_in_leave

from datetime import date

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.is_superuser:
            return Leave.objects.all()

        elif user.is_authenticated:
            junior_ids = user.juniors.values_list('id', flat=True)
            return Leave.objects.filter(employee__in=[user.id] + list(junior_ids))

        return Leave.objects.none()


    @action(detail=False, methods=['get'], url_path='user')
    def my_leaves(self, request):
        user = request.user
        leaves = Leave.objects.filter(employee=user).order_by('-start_date')
        serializer = self.get_serializer(leaves, many=True)
        return Response({
            "my_leaves": serializer.data if serializer.data else "No leaves found."
        }, status=200)


    @action(detail=False, methods=['get'], url_path='juniors')
    def juniors_leaves(self, request):
        junior_ids = request.user.juniors.values_list('id', flat=True)
        leaves = Leave.objects.filter(employee__in=junior_ids).order_by('-start_date')
        serializer = self.get_serializer(leaves, many=True)
        return Response({
            "juniors_leaves": serializer.data if serializer.data else "No junior leaves found."
        }, status=200)


    def perform_create(self, serializer):
        user = self.request.user
        leave = serializer.save(employee=user)

        # Deduct leave days
        try:
            leave_days = get_working_days_in_leave(leave.start_date, leave.end_date)
            today = date.today()

            if leave.start_date.month == today.month:
                user.leaves_available_this_month -= leave_days
            elif leave.start_date.month == (today.month + 1) % 12:
                user.leaves_available_next_month -= leave_days

            user.save()
        except Exception as e:
            pass  # You may log this

        # Send Notification
        try:
            Notification.objects.create(
                receiver=leave.employee.senior,
                message=(
                    f"{leave.employee.email} applied for leave "
                    f"from {leave.start_date} to {leave.end_date} "
                    f"on {leave.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
                ),
                sender=user
            )
        except Exception:
            pass


    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            old_leave = Leave.objects.get(pk=instance.pk)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            new_leave = serializer.instance
            update_user_leaves_on_update(old_leave, new_leave)

            new_leave.status = 'PENDING'
            new_leave.save()

            return Response({
                "message": "Leave updated successfully.",
                "data": LeaveSerializer(new_leave, context=self.get_serializer_context()).data
            }, status=200)

        except ValidationError as ve:
            return Response({"message": ve.detail}, status=200)
        except Exception as e:
            return Response({"message": f"Unexpected error: {str(e)}"}, status=200)


    def destroy(self, request, *args, **kwargs):
        try:
            leave = self.get_object()
            adjust_user_leaves_on_cancel(leave)
            leave.delete()
            return Response({"message": "Leave cancelled and days restored."}, status=200)
        except Exception as e:
            return Response({"error": f"Deletion failed: {str(e)}"}, status=200)


    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        try:
            leave = self.get_object()
            adjust_user_leaves_on_cancel(leave)
            leave.delete()
            return Response({"message": "Leave cancelled and days restored."}, status=200)
        except Exception as e:
            return Response({"error": f"Cancel failed: {str(e)}"}, status=200)


    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        '''
        Used to approve the leave of junior.
        '''
        try:
            leave = self.get_object()
            user = request.user

            if leave.employee.senior != user and not user.is_admin:
                return Response({'error': 'Not authorized to approve this leave.'}, status=200)

            if leave.status != 'PENDING':
                return Response({'error': 'Leave is already processed.'}, status=200)

            leave.status = 'APPROVED'
            leave.approved_by = user
            leave.save()

            return Response({'message': 'Leave approved successfully.'}, status=200)

        except Exception as e:
            return Response({'error': f'Approval failed: {str(e)}'}, status=200)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        '''
        Used to reject the leave of junior.
        '''
        try:
            leave = self.get_object()
            user = request.user

            if leave.employee.senior != user and not user.is_admin:
                return Response({'error': 'Not authorized to reject this leave.'}, status=200)

            if leave.status != 'PENDING':
                return Response({'error': 'Leave is already processed.'}, status=200)

            leave.status = 'REJECTED'
            leave.approved_by = user
            leave.save()

            return Response({'message': 'Leave rejected successfully.'}, status=200)

        except Exception as e:
            return Response({'error': f'Rejection failed: {str(e)}'}, status=200)
