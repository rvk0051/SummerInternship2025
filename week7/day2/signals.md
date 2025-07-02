# Django Signals: pre-save & post-save

## What are Signals?

Signals let Django apps send and receive notifications when certain actions occur, such as when a model is saved or deleted.  
They help you react to changes in your models without modifying their logic directly.

---

## Common Use Cases

| Signal     | Example Use Case                            |
|------------|---------------------------------------------|
| pre_save   | Auto-generate a slug before saving          |
| post_save  | Send a welcome email after user is created  |

---

## How to Use Django Signals

### Step 1: Import Required Tools

```
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
```

### Step 2: Write Signal Functions

post_save Example — Send email after user is created
```
@receiver(post_save, sender=get_user_model())
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"Welcome email sent to {instance.email}")
```

pre_save Example — Set default username if empty
```
@receiver(pre_save, sender=get_user_model())
def set_username_if_missing(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.email.split('@')[0]
```
* **sender -** The model class triggering the signal
* **instance -** The model instance being saved
* **created -** Boolean: True if it's a new record
* **kwargs -** Extra arguments passed by Django

### Step3: After Signals, edit apps.py
Create a signals.py file in your app.

Import the signal functions in apps.py to ensure they run when the app loads.
```
# apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  # <- import your signal handlers here
```

## Diagram: Signal Flow

Model Save Called

↓

pre_save signal → modify instance

↓

Model Saved

↓

post_save signal → trigger side-effects (emails, logs)