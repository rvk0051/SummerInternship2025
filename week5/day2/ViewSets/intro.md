# ViewSets in DRF
In Django REST Framework (DRF), ViewSets are a powerful abstraction designed to streamline the development of API endpoints. A ViewSet allows you to combine the logic for handling multiple HTTP methods in a single class. Instead of writing separate views for GET, POST, PUT, DELETE, etc., you bundle them into a ViewSet.

### Example:-
```aiignore
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

```
'ModelViewSet' provides full default implementations for list, create, retrieve, update, partial update, and destroy actions.

## Why use ViewSets?
* They automate much of CRUD (Create, Read, Update, Delete) logic.
* They integrate seamlessly with DRF routers, which we'll discuss in the next part.
* They improve maintainability by grouping related API logic.