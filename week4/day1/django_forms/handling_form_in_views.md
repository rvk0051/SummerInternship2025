# Handling the Form in a View 
In views,
* we display the form when the user visits the page.
* and we handle the user’s submitted data when they click submit.

### Example:-
# views.py
    from django.shortcuts import render
    from .forms import ContactForm

    def contact_view(request):
        if request.method == 'POST':
            # Form submitted by user
            form = ContactForm(request.POST)  # creates object of the form 'ContactForm'
            if form.is_valid():  # if form holds the valid data
                # If all validations pass
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                print(name, email, message)  # Process the data (email/save etc.)
        else:
            # Initial page visit
            form = ContactForm() # If user just opened the page, give them a fresh empty form
    
        return render(request, 'contact.html', {'form': form})

##### If the form submitted is valid, 
Django gives clean Python values in a dictionary called 'cleaned_data'.

##### If the form submitted is not valid,
* form.is_valid() becomes False.
* Django stores error messages in form.errors

 **Example:-**

        <form method="post">
          {% csrf_token %}
  
          {{ form.non_field_errors }}
  
          {{ form.name.label }}<br>
          {{ form.name }}
          {{ form.name.errors }}

          <br><br>

          {{ form.email.label }}<br>
          {{ form.email }}
          {{ form.email.errors }}

          <br><br>

          {{ form.message.label }}<br>
          {{ form.message }}
          {{ form.message.errors }}

          <button type="submit">Send</button>
        </form>

Example Output:-
Name: [Your Name Here]
This field is required.
