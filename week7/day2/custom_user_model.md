# Custom User Model in Django

## What is a Custom User Model?

A Custom User Model in Django is a user-defined model that replaces Django's default User model, allowing you to change the authentication field (like using email instead of username) and add additional fields (like phone number, profile image, etc.) based on your project’s needs.

## Why Use a Custom User Model?

| Reason                          | Benefit                                |
|--------------------------------|-----------------------------------------|
| Use email instead of username  | Modern login experience                 |
| Add custom fields              | Store profile data directly in User     |
| Full control over auth         | Override login, creation, permissions   |
| Better scalability             | Avoid complex migrations later          |

## When to Use It?

Always use a custom user model at the start of your project if you expect any customization, it is not easier later.

## How to Create a Custom User Model

Step 1: Create the Model
```
# users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    # Used to create normal users
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')  # Ensure email is mandatory
        email = self.normalize_email(email)            # Normalize the email (e.g. lowercase domain)
        user = self.model(email=email, **extra_fields) # Create a user instance with given email and extra fields
        user.set_password(password)                    # Hash the password before storing
        user.save()                                    # Save user to DB
        return user

    # Used to create admin/superusers
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)       # Superuser must be staff
        extra_fields.setdefault('is_superuser', True)   # Superuser must have all permissions

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)  # Delegate to create_user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)             # Use email instead of username
    name = models.CharField(max_length=255)            # Custom field for user's name
    is_active = models.BooleanField(default=True)      # Required field for login status
    is_staff = models.BooleanField(default=False)      # Determines admin access

    objects = CustomUserManager()                      # Use our custom manager

    USERNAME_FIELD = 'email'                           # Define the unique identifier for auth
    REQUIRED_FIELDS = ['name']                         # Fields required when creating a superuser

    def __str__(self):
        return self.email                              # String representation of the user

```

Step 2: Register the Custom User Model
```
# In your settings.py:

AUTH_USER_MODEL = 'users.CustomUser'
```
Step 3: Create and Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Admin Integration (Optional)
```
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
```

## Common Mistakes to Avoid

* Forgetting to set AUTH_USER_MODEL before the first migration.
* Importing User directly instead of using get_user_model().
* Not writing a CustomUserManager with create_user and create_superuser methods.

