from django.urls import path
from .views import (
    CheckInView,
    CheckOutView,
    AttendanceByDateView,
)

urlpatterns = [
    path('check-in/', CheckInView.as_view(), name='check-in'),
    path('check-out/', CheckOutView.as_view(), name='check-out'),
    path('my-attendance/', AttendanceByDateView.as_view(), name='attendance-by-date'),
]
