from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Account APIs (register/login)
    path('api/auth/', include('accounts.urls')),

    # Notes & folders APIs
    path('api/notes/', include('notes.urls')),
]