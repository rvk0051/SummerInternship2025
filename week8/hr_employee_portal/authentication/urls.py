from .views import RegisterView, LoginView, CurrentUserView, JuniorUserView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Custom login view using DRF token
    path('user_data/', CurrentUserView.as_view(), name='user_data'),
    path('user_juniors/', JuniorUserView.as_view(), name='user_juniors'),
]
