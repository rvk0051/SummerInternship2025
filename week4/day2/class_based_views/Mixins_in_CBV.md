# Mixins in CBVs
A mixin is a class that provides methods that can be used by other classes. In Django, mixins are typically used to add specific functionality to class-based views. They can be combined with other mixins or views to create complex behaviors.

#### Example:-
1. LoginRequiredMixin: Ensures that a user is authenticated before accessing a view.
2. PermissionRequiredMixin: Checks if a user has a specific permission before allowing access to a view.
3. UserPassesTestMixin: Allows you to define a custom test to determine if a user can access a view.
4. FormMixin: Provides functionality for handling forms in views.

#### Usage of Mixins example
##### 1. LoginRequiredMixin:-

This mixin ensures that only authenticated users can access a view.

    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.views.generic import ListView
    from .models import MyModel
    class MyModelListView(LoginRequiredMixin, ListView):
        model = MyModel
        template_name = 'myapp/mymodel_list.html'
        login_url = '/login/'  # Redirect to this URL if not logged in

##### 2. UserPassesTestMixin:-
  
This mixin allows you to define a custom test for user access.

    from django.contrib.auth.mixins import UserPassesTestMixin
    from django.views.generic import UpdateView
    from .models import MyModel

    class MyModelUpdateView(UserPassesTestMixin, UpdateView):
        model = MyModel
        template_name = 'myapp/mymodel_form.html'
    
        def test_func(self):
           # Custom test logic
           return self.request.user.is_superuser  # Only superusers can access this view

## Creating Your Own Mixin
One creates one's own Mixins also to encapsulate common functionality. 

##### Example:-
Creating a simple mixin that adds a context variable to the view.

    class CustomContextMixin:
        def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           context['custom_variable'] = 'This is a custom context variable'
           return context

    class MyModelListView(CustomContextMixin, ListView):
        model = MyModel
        template_name = 'myapp/mymodel_list.html'


