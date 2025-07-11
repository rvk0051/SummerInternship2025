from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from decimal import Decimal
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
        status_param = request.query_params.get('status')  # ?status=Pending
        leaves = Leave.objects.filter(employee=user)
        if status_param:
            leaves = leaves.filter(status=status_param)
        leaves = leaves.order_by('-start_date')
        serializer = self.get_serializer(leaves, many=True)
        return Response({
            "my_leaves": serializer.data if serializer.data else "No leaves found."
        }, status=200)


    @action(detail=False, methods=['get'], url_path='juniors')
    def juniors_leaves(self, request):
        junior_ids = request.user.juniors.values_list('id', flat=True)
        status_param = request.query_params.get('status')  # ?status=Approved
        leaves = Leave.objects.filter(employee__in=junior_ids)
        if status_param:
            leaves = leaves.filter(status=status_param)
        leaves = leaves.order_by('-start_date')
        serializer = self.get_serializer(leaves, many=True)
        return Response({
            "juniors_leaves": serializer.data if serializer.data else "No junior leaves found."
        }, status=200)

    def create(self, request, *args, **kwargs):
        """
        Create leave with all validation. Always return status 200.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = request.user
            validated_data = serializer.validated_data

            from datetime import date
            today = date.today()

            start_date = validated_data.get('start_date')
            end_date = validated_data.get('end_date')
            is_half_day = validated_data.get('is_half_day', False)
            is_start_half_day = validated_data.get('is_start_half_day', False)
            is_end_half_day = validated_data.get('is_end_half_day', False)

            # Calculate leave days
            leave_days, holidays = get_working_days_in_leave(
                start_date,
                end_date,
                is_start_half_day,
                is_end_half_day
            )

            # Validation: All dates are weekends
            if leave_days == 0.0:
                return Response({
                    "message": "Leave not allowed: selected dates are weekends only.",
                    "leave_days": 0.0,
                    "holidays": [d.strftime('%Y-%m-%d') for d in holidays]
                }, status=200)

            # Validation: Half-day only for one day leave
            if leave_days >= 1 and is_half_day:
                return Response({
                    "message": "Half day leave can only be applied for a single day.",
                    "leave_days": leave_days,
                    "holidays": [d.strftime('%Y-%m-%d') for d in holidays]
                }, status=200)

            # Save the leave
            leave = serializer.save(employee=user)

            # Update leave balance
            if leave.start_date.month == today.month:
                user.leaves_available_this_month -= Decimal(f"{leave_days}")
            elif leave.start_date.month == (today.month + 1) % 12:
                user.leaves_available_next_month -= Decimal(f"{leave_days}")
            user.save()

            # Send notification to senior
            try:
                Notification.objects.create(
                    receiver=leave.employee.senior,
                    sender=user,
                    message=(
                        f"{user.email} applied for leave "
                        f"from {leave.start_date} to {leave.end_date} "
                        f"on {leave.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
                    )
                )
            except Exception as notif_error:
                print("Notification error:", notif_error)

            return Response({
                "message": "Leave applied successfully.",
                "leave_days": leave_days,
                "holidays": [d.strftime('%Y-%m-%d') for d in holidays],
                "data": LeaveSerializer(leave, context=self.get_serializer_context()).data
            }, status=200)

        except Exception as e:
            return Response({
                "message": f"Failed to apply leave: {str(e)}"
            }, status=200)

    def update(self, request, *args, **kwargs):
        # user updates their leave
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
        # overriding default function for deleting leave
        try:
            leave = self.get_object()
            adjust_user_leaves_on_cancel(leave) # Restore user's leave balance (custom logic)
            leave.delete()
            return Response({"message": "Leave cancelled and days restored."}, status=200)
        except Exception as e:
            return Response({"error": f"Deletion failed: {str(e)}"}, status=200)


    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        # Function made for deleting leave
        try:
            leave = self.get_object()
            adjust_user_leaves_on_cancel(leave) # Restore user's leave balance (custom logic)
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
            today = date.today()
            leave_days, _ = get_working_days_in_leave(
                leave.start_date,
                leave.end_date,
                leave.is_start_half_day,
                leave.is_end_half_day
            )
            user = leave.employee
            if leave.start_date.month == today.month:
                user.total_leave_days_in_this_month += Decimal(str(leave_days))
            elif leave.start_date.month == (today.month + 1) % 12:
                user.leaves_available_next_month -= Decimal(str(leave_days))
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
