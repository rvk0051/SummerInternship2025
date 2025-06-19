from django.contrib import admin
from .models import Folder, Note

# Register models for Django admin
admin.site.register(Folder)
admin.site.register(Note)

