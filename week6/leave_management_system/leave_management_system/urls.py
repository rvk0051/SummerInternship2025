from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth-related
    path('api/auth/', include('authentication.urls')),

    # Leave-related
    path('api/', include('leave_management.urls')),

]

