from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from ..models import Leave, Notification
from ..serializers import LeaveSerializer


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
        try:
            serializer.is_valid(raise_exception=True)
            leave = serializer.save(employee=request.user)

            try:
                Notification.objects.create(
                    receiver=leave.employee.senior,
                    message=(
                        f"{leave.employee.email} applied for leave "
                        f"from {leave.start_date} to {leave.end_date} "
                        f"on {leave.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
                    ),
                    sender=request.user
                )
            except Exception:
                pass  # Optional: log error

            return Response({
                "message": "Leave applied successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            return Response({"message": ve.detail}, status=200)
        except Exception as e:
            return Response({"message": f"Unexpected error: {str(e)}"}, status=200)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial, context=self.get_serializer_context())
        try:
            serializer.is_valid(raise_exception=True)
            leave = serializer.save()
            leave.status = 'PENDING'  # Reset to pending on any update
            leave.save()

            return Response({
                "message": "Leave updated successfully.",
                "data": LeaveSerializer(leave, context=self.get_serializer_context()).data
            }, status=200)

        except ValidationError as ve:
            return Response({"message": ve.detail}, status=200)
        except Exception as e:
            return Response({"message": f"Unexpected error: {str(e)}"}, status=200)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
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
