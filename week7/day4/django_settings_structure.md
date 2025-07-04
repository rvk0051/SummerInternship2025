# Django Settings Structure (Local vs Production)

For different purpose (for developement, testing and for production), we neeed local.py and production.py which have respective settings.

## Purpose

A Django project typically runs in multiple environments:

- **Local** (development): For building, testing, and debugging.
- **Production** (live): For real users in a secure and stable environment.

Each environment requires different settings, so separating them keeps your project clean, scalable, and secure.

---

## Recommended Structure

Instead of settings.py, make folder of settings, having 3 files '__init__.py', 'local.py', 'production.py'.

settings/
├── init.py
├── base.py # Shared/common settings
├── local.py # Development-specific settings
└── production.py # Production-specific settings


---

## Settings Breakdown

### base.py

This file contains settings **common to all environments**.

```
# project/settings/base.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    ...
]

MIDDLEWARE = [
    ...
]

TEMPLATES = [
    ...
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Placeholder for override
DATABASES = {}
```

### local.py
```aiignore
# project/settings/local.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

### production.py
```aiignore
# project/settings/production.py
from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}

# Security Settings
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## set 'DJANGO_SETTINGS_MODULE':-
We need to set 'DJANGO_SETTINGS_MODULE' for local and for production accordingly.
These are 3 ways:-

### 1. '.env' file:-
In '.env' file, whenever your purpose changes,i.e.; changes from local to production or vice-versa, 
you need to change `DJANGO_SETTINGS_MODULE=project.settings.local` to `DJANGO_SETTINGS_MODULE=project.settings.production` or vice-versa.

### 2. manage.py (for Local Development), wsgi.py or asgi.py (for Production)
**In manage.py:-**
For local development, set `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.local')` in manage.py.

**In wsgi.py or asgi.py:-**
For production, set `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')` in wsgi.py or asgi.py.

### 3. Use CMD:-
Use this command in cmd always when production is needed and:-
`set DJANGO_SETTINGS_MODULE=project.settings.production`

and when local development or testing is needed, set it to local but this will be needed everytime, user will run the project on server.

 

