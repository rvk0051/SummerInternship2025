from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ContactHRListCreateAPIView,
    ContactHRDetailAPIView,
    MarkAsResolvedAPIView
)

urlpatterns = [
    path('contact/', ContactHRListCreateAPIView.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', ContactHRDetailAPIView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/mark_resolved/', MarkAsResolvedAPIView.as_view(), name='mark-as-resolved'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
