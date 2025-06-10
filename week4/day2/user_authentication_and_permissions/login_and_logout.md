# Login and Logout in Django
Django gives you ready-made views for login/logout, but you can also make your own custom login form.

## Built-in login and logout:-
Django comes with 'LoginView' for logging in and 'LogoutView' for logging out. 
These handle sessions automatically.
These both views are located in `django.contrib.auth/views/auth_views`.

### Set-up:-

#### 1. Add URLs for Login and Logout:-
    # project/urls.py
    from django.contrib.auth import views as auth_views
    from django.urls import path

    urlpatterns = [
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]

/login/ → show login page and authenticate user
/logout/ → clear session and log user out

#### 2. Create login template:-
By default, to login, Django will look for the path which must be `templates/registration/login.html` for the built-in LoginView to automatically find it.

#### 3. Set Redirection URLs in settings.py
in settings.py, set redirection URLs that is set wherever you want the user to move after login or logout:- 
      
    LOGIN_REDIRECT_URL = '/'            # After successful login
    LOGOUT_REDIRECT_URL = '/login/'     # After logout
You could change these addresses.
