# 1. Register Your Models
'''
To make models accessible in the admin interface, it is needed to register them in the admin.py file of your app.
Here’s an example using the 'Post' model we defined in 'django_admin.md'
'''
# Example:
from django.contrib import admin
from models import Post

admin.site.register(Post)

# 2. Customize the Admin Interface
'''
You can customize the admin interface for your models by creating a custom admin class.
'''
# Example:
from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Fields to display in the list view
    search_fields = ('title', 'content')     # Fields to search
    list_filter = ('created_at',)            # Filters to apply in the sidebar

admin.site.register(Post, PostAdmin)

# 3. Inline Editing
'''
Inline editing allows one to edit related fields in the same form as the parent object.
If one have related models, one can enable inline editing in the admin interface
'''
# Example:
from django.db import models

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty forms to display

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    inlines = [CommentInline]  # Enable inline editing for comments

admin.site.register(Post, PostAdmin)