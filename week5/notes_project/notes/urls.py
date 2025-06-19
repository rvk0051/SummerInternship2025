from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FolderViewSet, NoteViewSet

# Create a DRF router instance
router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folder')
router.register(r'notes', NoteViewSet, basename='note')

# Including the router-generated URLs
urlpatterns = [
    path('', include(router.urls)),
]
