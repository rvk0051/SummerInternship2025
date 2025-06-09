# ModelForm
Django ModelForm is a class that is used to directly convert a model into a Django form.
If you’re building a database-driven app, chances are you’ll have forms that map closely to Django models

##### Example:
   
     # models.py
     from django.db import models

     class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField()

Creating form:-

     # forms.py
     from django import forms
     from .models import Contact

    class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

Meta class tells Django:
* Which model to use
* which fields to include in the form

you could use these also:- 

`fields = '__all__'`  to include all fields

``exclude = ['created_at']`` to exclude some fields
