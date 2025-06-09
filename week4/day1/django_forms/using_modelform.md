# Using ModelForm in View

##### Example:-

    # views.py
    from django.shortcuts import render, redirect
    from .forms import ContactForm

    def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  # 💥 creates & saves Contact object
                return redirect('thank_you')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})

### form.save():-
* Creates a new instance of the model
* Fills it with the validated cleaned_data
* Saves it to the database!