# URL Routing
In Django, URL routing is the mechanism that maps URLs to views. This is done using the urls.py file in Django application.

## Working:-

#### 1. Creating a URLconf: 
A URLconf is a mapping between URL patterns and views. Define this in a urls.py file.

#### 2. Defining URL Patterns: 
Use the path() or re_path() functions to define URL patterns. The path() function is used for simpler, more readable patterns, while re_path() allows for more complex regular expressions.

##### Example:-
   
    from django.urls import path
    from . import views

    urlpatterns = [
       path('', views.home, name='home'),  # Maps the root URL to the home view
       path('about/', views.about, name='about'),  # Maps /about/ to the about view
       path('articles/<int:id>/', views.article_detail, name='article_detail'),  # Dynamic URL
    ]

#### 3. Including Other URLconfs: 
Other URLconf modules could be included using the include() function. This is useful for organizing URLs into different apps.

##### Example:-
    from django.urls import include

    urlpatterns = [
       path('blog/', include('blog.urls')),  # Includes URLs from the blog app
    ]

## URL routing in Django REST Framework:-
Django REST Framework builds on Django's URL routing but is specifically designed for building RESTful APIs. Here’s how URL routing works in DRF:

* #### Using Routers: 
DRF provides a powerful feature called routers that automatically create URL patterns for API views based on `viewsets`.

* #### Creating a ViewSet: 
A ViewSet is a class that defines the behavior of API endpoints. Typically create a ViewSet by subclassing `viewsets.ModelViewSet`.

##### Example:-
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import ArticleViewSet

    router = DefaultRouter()
    router.register(r'articles', ArticleViewSet)  
    # Automatically creates routes for the ArticleViewSet which includes routes for listing, creating, retrieving, updating, and deleting articles

    urlpatterns = [
        path('', include(router.urls)),  # Includes all the routes from the router
    ]

* #### Customizing Routes: 
Routes could be customized by defining own URL patterns alongside the router.