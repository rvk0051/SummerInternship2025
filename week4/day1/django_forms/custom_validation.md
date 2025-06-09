# Custom Validation with clean_<field>() and clean()

Although Django itself validates for required fields and field types, custom validations could be added.

## clean_<field>(): Field-Level Custom Validation
Use this when you want to validate a single field.

##### Example:-
   
    class ContactForm(forms.Form):
       name = forms.CharField()
       email = forms.EmailField()

       def clean_name(self):
          data = self.cleaned_data['name']
          if data.lower() == 'admin':
             raise forms.ValidationError("Name cannot be 'admin'")
          return data  # must return cleaned value

Django runs this method automatically, if it raises ValidationError, form becomes invalid, it else moves on.

## clean(): Form-Wide Custom Validation:-

we use this when- 
* You need to compare multiple fields
* Or do a validation that involves more than one input

##### Example:-
   
    class SignupForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)

        def clean(self):
            cleaned_data = super().clean()
            pwd = cleaned_data.get("password")
            cpwd = cleaned_data.get("confirm_password")

            if pwd != cpwd:
               raise forms.ValidationError("Passwords do not match")

To use this and show errors, use this in templates:-

    {% if form.non_field_errors %}
       <div class="error">
          {{ form.non_field_errors }}
       </div>
    {% endif %}
