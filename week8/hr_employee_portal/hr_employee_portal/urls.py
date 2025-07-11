"""
URL configuration for hr_employee_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # URls of 'authentication' app
    path('api/auth/', include('authentication.urls')),

    # URls of 'leave_management' app
    path('api/', include('leave_management.urls')),

    # URls of 'attendance' app
    path('api/attendance/', include('attendance_system.urls')),

    # URLs of 'contact_hr' app
    path('api/', include('contact_hr.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
