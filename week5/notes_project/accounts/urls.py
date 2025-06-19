from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    # Route for user registration
    path('register/', RegisterView.as_view()),

    # Route for user login
    path('login/', LoginView.as_view()),
]
