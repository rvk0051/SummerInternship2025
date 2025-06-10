# Class-Based Views(CBVs) in Django
In Django, there are two main ways to handle views:
* Function-Based Views (FBVs): You define views using functions.
* Class-Based Views (CBVs): You define views using classes.

A Class-Based View (CBV) is a Python class that inherits from Django's base view classes to handle web requests (GET, POST, etc.) in an organized and reusable way.

CBVs should be used when,
* When your view logic is complex.
* When you want to reuse code across views.
* When you want to use Django’s built-in Generic Views (like ListView, DetailView, etc.).

Example:-
    
Defining  CBV in views.py,

    from django.http import HttpResponse
    from django.views import View
    
    # creating CBV
    class WelcomeLibraryView(View):
        def get(self, request):
            return HttpResponse("Welcome to Online Library!")

* 'View' is a base class provided by Django.

Mapping the CBV in URLs,

    # urls.py
    from django.urls import path
    from .views import WelcomeLibraryView

    urlpatterns = [
        path('library/', WelcomeLibraryView.as_view(), name='library-welcome'),
    ]

* '.as_view()' is a class method of the View class. Converts your class to a Django-compatible view function. Internally calls dispatch()
* get()/post() -> Handle respective HTTP methods.
* User sends a GET/POST → dispatch() calls get()/post() respectively.
* dispatch() is a Core method that decides which HTTP method to call (get(), post(), etc.)



