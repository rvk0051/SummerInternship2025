# Import required Django admin module and model
from django.contrib import admin
from .models import Profile
from .models import Post

# Register the Post model with the default admin interface
admin.site.register(Post)

# Register Profile model with custom admin configuration using decorator syntax
@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    # Configure which fields to display in the admin list view
    list_display = ['user', 'author_name']
    
    # Configure which fields can be used for searching profiles
    # user__username allows searching through related User model's username field
    search_fields = ['author_name', 'user__username']