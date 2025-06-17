# Mixin
In Django REST Framework (DRF), mixins are a set of reusable classes that provide common functionality for view classes. They allow you to create views that handle specific HTTP methods (like GET, POST, PUT, DELETE) without having to write the same code repeatedly. Mixins promote code reuse and help keep your views clean and organized.

## Why Use Mixins?
* Code Reusability: 
Mixins allow you to reuse common functionality across different views, reducing code duplication.
* Separation of Concerns: 
They help separate different behaviors into distinct classes, making your code easier to maintain and understand.
* Flexibility: 
You can combine multiple mixins to create views that have the desired behavior without being tied to a specific class hierarchy.

## Some of the mixins in DRF:-
1. CreateModelMixin: 
Provides the create method to handle POST requests for creating new instances.
2. RetrieveModelMixin: 
Provides the retrieve method to handle GET requests for retrieving a single instance.
3. UpdateModelMixin: 
Provides the update method to handle PUT and PATCH requests for updating an instance.
4. DestroyModelMixin: 
Provides the destroy method to handle DELETE requests for deleting an instance.
5. ListModelMixin: 
Provides the list method to handle GET requests for listing multiple instances.

## Example:-
Let's say we have a simple Task model, and we want to create a view that allows us to list, create, retrieve, update, and delete tasks. We can use mixins to achieve this.

```aiignore
# serializers.py
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # 'Task' is a model
        fields = ['id', 'title', 'description', 'completed']

```

```aiignore
# views.py
from rest_framework import mixins, generics

class TaskListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

```

