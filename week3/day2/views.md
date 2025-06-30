# Views
The views.py file in a Django application contains the logic for processing incoming requests and returning responses. It acts as the intermediary between the models (which define the data) and the templates (which define how the data is presented). In essence, views determine what data to display and how to display it.

## Types of Views:-
### 1. Function-Based Views (FBVs):
Simple Python functions that accept a request object and return a HttpResponse or render a template.
However, you would typically use DRF's response classes to return data in a more API-friendly format.
Example:- 

     from django.shortcuts import render
     from .models import Article

     def article_list(request):
       articles = Article.objects.all()
       return render(request, 'articles/list.html', {'articles': articles})
   
### 2. Class-Based Views (CBVs):
Views implemented as classes that provide more structure and reusable functionality. 
Django provides generic CBVs like ListView, DetailView, or it could be user-defined.
Example:-

    from django.views.generic import ListView
    from .models import Article

    class ArticleListView(ListView):
       model = Article
       template_name = 'articles/list.html'
       context_object_name = 'articles'

If drf is needed to use:- DRF provides a set of generic class-based views that simplify the creation of common API endpoints. For example, you can use APIView or the more specialized views like ListAPIView, RetrieveAPIView, etc.
Example:-
       
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class MyAPIView(APIView):
       def get(self, request):
           return Response({"message": "Hello, World!"})
   
   
### 3. ViewSets: 
ViewSets are Class-Based Views designed for building REST APIs.

DRF introduces the concept of ViewSets, which combine the logic for handling multiple related views into a single class. This is particularly useful for CRUD operations.
Example:-

     from rest_framework import viewsets
     from .models import MyModel
     from .serializers import MyModelSerializer
     class MyModelViewSet(viewsets.ModelViewSet):
        queryset = MyModel.objects.all()
        serializer_class = MyModelSerializer
   
