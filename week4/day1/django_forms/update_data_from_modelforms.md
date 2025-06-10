# Updating data using ModelForms
Data in the database could be updated using ModelForms
and we use the ModelForms when we want to:
* Pre-fill a form with existing data
* Let the user make changes
* Save updates back to the database

##### Example:-
# views.py
    from django.shortcuts import render, get_object_or_404, redirect
    from .models import Contact
    from .forms import ContactForm

    def edit_contact(request, id):

        contact = get_object_or_404(Contact, pk=id, user=request.user)
fetching object from the data using the id, if the object doesn't exist, it will return a 404 error.

        if request.method == 'POST':
            form = ContactForm(request.POST, instance=contact)
Create a form, and pre-fill it with this object's current data.

            if form.is_valid():
                form.save()
                return redirect('contact_detail', id=contact.id)
        else:
            form = ContactForm(instance=contact)

        return render(request, 'edit_contact.html', {'form': form})

for getting the id, we use the following in the URL:

    path('edit/<int:id>/', views.edit_contact, name='edit_contact')