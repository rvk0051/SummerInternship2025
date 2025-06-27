from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
    LeaveRequestViewSet,
    NotificationViewSet
)

# urls get auto-generated in routers.
router = DefaultRouter()
router.register(r'leaves', LeaveRequestViewSet, basename='leave')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('notifications/mark-all-read/', NotificationViewSet.as_view({'post': 'mark_all_read'}), name='notifications-mark-all-read'),
    path('notifications/mark-as-read/', NotificationViewSet.as_view({'post': 'mark_as_read'}),
         name='notifications-mark-as-read'),
    path('', include(router.urls)),
]