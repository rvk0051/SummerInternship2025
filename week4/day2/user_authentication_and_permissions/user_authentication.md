# User Authentication
User authentication is the process of verifying a user's identity to ensure they are who they claim to be before granting them access to a system or resource. This process is crucial for security and ensures that only authorized individuals can access sensitive information. 

# User Authentication in Djnago
Django comes with a built-in authentication system that handles user accounts, groups, permissions, and cookie-based user sessions.

## Setting Up Authentication
To use Django's authentication system, you need to ensure that the django.contrib.auth app is included in your INSTALLED_APPS in settings.py:
` INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    ...
]`

## Default User Model
Django provides a default user model (User) that includes fields like username, password, email, first name, and last name.

    class User(models.Model):
       username       = CharField(unique=True)
       password       = CharField()  # Stored as a hashed value
       email          = EmailField()
       first_name     = CharField()
       last_name      = CharField()
       is_staff       = BooleanField(default=False)
       is_superuser   = BooleanField(default=False)
       is_active      = BooleanField(default=True)
       date_joined    = DateTimeField()
       last_login     = DateTimeField()

You can create a user using the following

    from django.contrib.auth.models import User
    # You can create user like this:
    user = User.objects.create_user(username='john', password='pass1234')

## c. Custom User Model
To customize, create your own model and tell Django via AUTH_USER_MODEL.

in accounts/models.py:-

    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        age = models.IntegerField(null=True, blank=True)

in settings.py:- 
    
    AUTH_USER_MODEL = 'accounts.CustomUser'