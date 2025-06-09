# Django Forms
Django Forms are used to gather input from users, validate that input, and process it, often saving the data to the database. For example, when registering a user, a form collects information like name, email, and password.
## Why Django Forms?
In any web application, forms are how users input data: registration forms, login forms, contact forms, etc. Now you can manually build HTML forms and handle inputs using request.POST or request.GET — but that’s tedious and error-prone.

* Django Forms solve this by:
* Automatically generating HTML form fields
* Handling data validation (like checking for empty fields or correct email format)
* Cleaning and converting input data to Python types
* Providing easy error messages.
* Tightly integrating with Django models (ModelForm)

While you can build forms using raw HTML, Django Forms simplify form creation and validation, making your code cleaner and more secure.

## Types of Django forms

1. Forms (from django import forms)
Used when your form is independent of any model.

2. ModelForms
Used when your form is directly tied to a model — e.g., creating or editing a database object.