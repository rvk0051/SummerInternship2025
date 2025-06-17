# Types of ViewSets
## 1. rest_framework.viewsets.ViewSet:-
* This is the most basic ViewSet class. It provides no default implementations for any actions (list, create, etc.) or for handling queryset or serializer_class.
* Use ViewSet when your API logic doesn't directly map to a Django model or standard CRUD operations, or when you need complete control over every action. While it behaves similarly to rest_framework.views.APIView, its primary advantage is that it can be registered with a Router.

## 2. rest_framework.viewsets.GenericViewSet:-
* Inherits from ViewSet and mixes in functionality from rest_framework.generics.GenericAPIView. This means it provides core functionalities like get_object(), get_queryset(), get_serializer_class(), perform_create(), perform_update(), etc., which are common to generic views.
* Ideal when you want to define your custom actions (list, create, etc.) explicitly but still want the convenience of automatically handling the queryset and serializer_class attributes, along with helper methods for common operations.

## 3. rest_framework.viewsets.ModelViewSet:-
* This is the most commonly used and powerful ViewSet. It inherits from GenericViewSet and mixes in all the standard mixin classes (ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin).
* It automatically provides full CRUD (Create, Retrieve, Update, Delete) operations out-of-the-box for a specific model. For typical RESTful APIs interacting with Django models, ModelViewSet is the go-to choice. You primarily need to define the queryset and serializer_class.
