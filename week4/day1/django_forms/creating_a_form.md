# Creating a Django Form
Creating a form in Django is completely similar to creating a model, one needs to specify what fields would exist in the form and of what type. For example, to input, a registration form one might need First Name (CharField), Roll Number (IntegerField), and so on. 

### Syntax: 

    from django import forms
    class FormName(forms.Form):
         # each field would be mapped as an input field in HTML
         field_name = forms.Field(**options)

### Example:

    from django import forms
    class ContactForm(forms.Form):
        name = forms.CharField(max_length=100)
        email = forms.EmailField()
        message = forms.CharField(widget=forms.Textarea)

This creates a form with:
* A name field (text input)
* An email field (email input with validation)
* A message field (text area)