# Using Redis cache in a Django project on Windows:-
## Step 1: Install Redis on Windows
Redis doesn't officially support Windows, but you can run it using:

### Option A: Use Redis via WSL (Recommended)
1. Install WSL (Windows Subsystem for Linux):

Open PowerShell as admin and run:
`wsl --install`
(Restart your PC if required)

2. Install Ubuntu from Microsoft Store

3. Install Redis in WSL Ubuntu:

```
sudo apt update
sudo apt install redis-server
```

4. Start Redis server:

`sudo service redis-server start`

### Option B: Use Redis with Docker (Alternative)

Install Docker Desktop

Run Redis container:

`docker run -d -p 6379:6379 --name redis redis`

## Step 2: Install Required Python Package
In Django project's virtual environment, run:

`pip install django-redis`

## Step 3: Configure Redis in settings.py

Update your Django settings.py like this:

`CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}`

## Step 4: Use Redis Cache in Django
You can now cache views or data:

### 1. Using cache_page Decorator
```
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def my_view(request):
    ...
```

### 2. Low-level API

```
from django.core.cache import cache

cache.set('my_key', 'value', timeout=60)
value = cache.get('my_key')
```

## Step 5: Verify Redis is Working
Use this to test in your view or shell:
```
from django.core.cache import cache
cache.set("hello", "world", timeout=60)
print(cache.get("hello"))  # Output: 'world'
```
If this works, your Redis cache is running perfectly on Windows with Django!