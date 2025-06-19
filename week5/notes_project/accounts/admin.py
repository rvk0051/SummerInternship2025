from django.contrib import admin  # Django's admin site interface
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # Base class for custom user admin
from .models import CustomUser  # Importing CustomUser model

class UserAdmin(BaseUserAdmin):                              # Define how CustomUser will appear in admin
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')  # Columns shown in the admin list
    list_filter = ('is_staff', 'is_active')                  # Filters on right-hand side of admin
    ordering = ('email',)                                    # Default sort order in admin list
    search_fields = ('email', 'name')                        # Searchable fields in admin

    # Fields displayed when viewing/changing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Fields shown when creating a new user via admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

# Register the model and its admin customization
admin.site.register(CustomUser, UserAdmin)

admin.site.site_header = "NoteIt Admin Panel"
admin.site.site_title = "NoteIt"