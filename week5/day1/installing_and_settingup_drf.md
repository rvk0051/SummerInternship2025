# Installing DRF
Before installing DRF, make sure you have created a virtual environment and activated it as all the installations need to be done in that virtual environment.
Command to be run in your terminal for installing Django Rest Framework:-
`pip install djangorestframework`

# Setting up DRF
For setting up DRF in your Django project, add the following in the INSTALLED APPS of `settings.py`:-
`INSTALLED_APPS = [
    ...
    'rest_framework',
]
`
#  DRF's Login/Logout URLs for the Browsable API
DRF comes with a fantastic "Browsable API." This is a web-based interface that allows you to interact with your API directly from your browser, making it incredibly easy to test and debug your endpoints. For APIs that require authentication, including these URLs provides convenient login/logout functionality within the browsable API itself.

```
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your other URL patterns
    # path('your_app/', include('your_app.urls')),

    # DRF browsable API login/logout URLs
    path('api-auth/', include('rest_framework.urls')),
]
```