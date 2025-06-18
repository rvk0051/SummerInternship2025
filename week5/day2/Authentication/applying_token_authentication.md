# Applying Token Authentication:-
## 1.  Add rest_framework and rest_framework.authtoken to INSTALLED_APPS:-
Add the following in settings.py:-
```aiignore
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

```
## 2. Migrate to create Token model:-
Migrate to create token model by running this command in the terminal:-
```aiignore
python manage.py migrate

```

## 3.  Enable DRF’s Token Authentication:-
```aiignore
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

```
By default now, every API needs authentication unless permission is changed.
## 4. Create token for each user:-
Token could be created for user manually or auto.

#### Manual way:-
Use the following command for manually creating token:-
`python manage.py drf_create_token <username>`

If this command doesn’t exist, you can do it in the Django shell:
`python manage.py shell`

#### Automatic token creation:-
For automatic token creation, add the following code to signals.py,
```aiignore
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

```
You can verify this using Django shell:
```aiignore
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

u = User.objects.get(username='your_username')
print(Token.objects.get(user=u).key)

```