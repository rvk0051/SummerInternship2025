# Installing Bootstrap

We could install Bootstrap and integrate ot with UI:-
Steps for it are:-

##### 1. Install the package
run the following command in the terminal:-
`pip install django-bootstrap5`

##### 2. Add to INSTALLED_APPS in `settings.py`

```
INSTALLED_APPS = [
    ...
    "django_bootstrap5",
]
```

##### 3. Load the Bootstrap tag in your template

Add these lines in the <head> of the template:-
```
{% load bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
```

##### 4. Use Bootstrap classes in your templates
Now use any Bootstrap class (like container, form-control, btn, etc.) in any template that extends this base.