from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    dashboard,
    edit_profile,
)

# URL patterns for blog post management
post_patterns = [
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

# URL patterns for user management
user_patterns = [
    path('accounts/register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', edit_profile, name='edit-profile'),
]

# Combined URL patterns
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # Homepage
    path('post/', include(post_patterns)),  # Include all post patterns under 'post/'
    *user_patterns,
]