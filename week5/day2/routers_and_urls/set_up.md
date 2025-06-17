# Setting up routers
Set up routers in 3 steps:-
## 1. Create a ViewSet:
Define a viewset for your model, which will handle the CRUD operations.
## 2. Register the ViewSet with a Router: 
Use DRF's built-in routers to register your viewset.
## 3. Include the Router's URLs in your URLconf: 
Add the router's URLs to your project's URL configuration.

## Example:-
Let's continue with our Task model and create a viewset for it, then set up a router to handle the URLs.
### Step 1: Create a ViewSet:
```aiignore
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Using ModelViewSet to handle all CRUD operations
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
```
### Step 2: Set Up the Router
```aiignore
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# This viewset handles all CRUD operations for the Task model. It uses the TaskSerializer to serialize and deserialize data.
from .views import TaskViewSet

router = DefaultRouter() #  built-in router provided by DRF
router.register(r'tasks', TaskViewSet)

```
### Step 3: Include the Router's URLs in your URLconf
```
urlpatterns = [
    path('', include(router.urls)),
    # adds all the generated URL patterns from the router to your URL configuration.
]

```

DefaultRouter: This is a built-in router provided by DRF. It automatically generates the following URL patterns for the TaskViewSet:

* GET /tasks/ - List all tasks
* POST /tasks/ - Create a new task
* GET /tasks/{id}/ - Retrieve a specific task
* PUT /tasks/{id}/ - Update a specific task
* PATCH /tasks/{id}/ - Partially update a specific task
* DELETE /tasks/{id}/ - Delete a specific task