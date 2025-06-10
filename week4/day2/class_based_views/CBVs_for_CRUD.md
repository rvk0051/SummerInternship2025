# Class-Based Views for CRUD operations in Django
Django provides Class-Based Views for CRUD operations in Django:-
* ListView - Display a list of objects
* DetailView - Display a single object’s details
* CreateView - Display and process form to add object
* UpdateView - Display and process form to update
* DeleteView - 	Confirm and delete object

These views work directly with Django Models, so a lot of time is saved.

for e.g.; model is

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)

##### 1. ListView - show all books
In views.py,

       from django.views.generic import ListView
       from .models import Book

       class BookListView(ListView):
           model = Book
           template_name = 'library/book_list.html'
           context_object_name = 'books'

##### 2. DetailView - show single book
In views.py,

     from django.views.generic import DetailView

     class BookDetailView(DetailView):
         model = Book
         template_name = 'library/book_detail.html'
         context_object_name = 'book'

##### 3. CreateView - adding new book
In views.py,

     from django.views.generic.edit import CreateView
     from django.urls import reverse_lazy

     class BookCreateView(CreateView):
         model = Book
         fields = ['title', 'author']
         template_name = 'library/book_form.html'
         success_url = reverse_lazy('book-list')

##### 4. UpdateView – edit book
In views.py,

    from django.views.generic.edit import UpdateView

    class BookUpdateView(UpdateView):
        model = Book
        fields = ['title', 'author']
        template_name = 'library/book_form.html'
        success_url = reverse_lazy('book-list')

##### 5. DeleteView – delete book
In views.py,

    from django.views.generic.edit import DeleteView

    class BookDeleteView(DeleteView):
       model = Book
       template_name = 'library/book_confirm_delete.html'
       success_url = reverse_lazy('book-list')
##### reverse-lazy:-
'reverse_lazy()' doesn't immediately convert a URL pattern name into an actual URL string when the code is executed. Instead, it waits until the URL is actually needed.
Use of 'reverse()' directly in a class-level attribute of a CBV (like success_url) will try to resolve the URL before the URL patterns are fully loaded, leading to a NoReverseMatch error.