from .auth_views import RegisterView, LoginView
from .user_views import CurrentUserView, JuniorUserView

__all__= [
    'RegisterView',
    'LoginView',
    'JuniorUserView',
    'CurrentUserView'
]