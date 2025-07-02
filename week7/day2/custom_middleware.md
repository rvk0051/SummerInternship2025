
# What is Middleware?

Middleware in Django is a system for processing requests and responses globally. It acts like a wrapper around your views. You can use it to:
* Inspect or modify incoming requests before they reach the view
* Inspect or modify outgoing responses after the view has processed the request

Think of middleware as layers in a sandwich:

`Request Bread → Middleware Layers → View (Filling) → Middleware Layers → Response Bread`

## Diagram: Middleware Sandwich

+-------------------+
| Incoming Request  |
+-------------------+
         ↓
+------------------------+
|  Middleware (Before)   |
+------------------------+
         ↓
+-------------------+
|       View         |
+-------------------+
         ↓
+------------------------+
|  Middleware (After)    |
+------------------------+
         ↓
+-------------------+
|  Final Response   |
+-------------------+

## Types of Django Middleware

* **Built-in Middleware:** Comes with Django (e.g., SecurityMiddleware)

* **Custom Middleware:** Written by user as per the logic required.

## Why Use Middleware?

Use middleware when you want to:

| Use Case                         | Without Middleware                          | With Middleware                        |
|----------------------------------|----------------------------------------------|-----------------------------------------|
| Log every request                | Add log code in every view                   | Add once in middleware                 |
| Block users at night             | Write time checks in views                   | Block in middleware easily             |
| Add headers to response          | Manually modify each response                | Add in middleware for all responses    |
| Show maintenance message         | Add check everywhere                         | Do it once in middleware               |
| Catch and format all exceptions  | Wrap every view in `try/except`              | Handle once in middleware              |

Middleware = global logic without duplication

## How to Create Custom Middleware

### Step 1: Create a Middleware Class

```
# myapp/middleware.py

class <CustomMiddlewareName>:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Middleware initialized")

    def __call__(self, request):
        print("Request received")
        response = self.get_response(request)
        print("Response ready")
        return response
```
* __init__() is called once when the server starts.
* __call__() is called every time a request comes in.

### Step 2: Register Middleware in settings.py
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    '<app_name>.middleware.<customized_middleware_name>',  # Add this line
]
```
 
## Real Example: Block Nighttime Access

```
from datetime import datetime
from django.http import HttpResponse

class BlockNightMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hour = datetime.now().hour
        if hour >= 22 or hour < 6:
            return HttpResponse("Site closed during night hours.")
        return self.get_response(request)
```

## Understanding __call__()

The __call__() method makes the middleware class callable, like a function.

### Django's Internal Flow:

`middleware_instance = <customized_middleware_name>(get_response)
response = middleware_instance(request)  # this calls __call__()`

So you never call __call__() manually — Django does it when handling requests.