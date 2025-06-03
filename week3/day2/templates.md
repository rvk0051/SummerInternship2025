# Django Templates
Django templates are the "T" in Django's MVT (Model-View-Template) architectural pattern. They are essentially HTML files (or any text-based format) that contain special Django template language (DTL) syntax. This syntax allows you to:

* ### Display dynamic data: 
Use `{{ variable_name }}` to insert data passed from your Django views.
* ### Control flow: 
Implement logic like` {% if condition %} `for conditional rendering or `{% for item in list %}` for iterating over data.

* ### Extend and include:
`{% extends 'base.html' %}` allows child templates to inherit from a base template, promoting code reuse and consistency across your site.
`{% include 'snippet.html' %}` allows you to insert content from another template file.

* ### Apply filters: 
Modify or format variable values using filters like `{{ my_date|date:"F j, Y" }}`.

* ### Use built-in tags: 
Django provides a rich set of built-in tags for various functionalities (e.g., `{% csrf_token %}` for security forms).

* ### Custom tags and filters: 
You can create your own custom template tags and filters to extend the DTL's capabilities.

## Configuration:

You configure template engines in your project's settings.py file, within the TEMPLATES setting. This typically involves specifying:

* BACKEND: 
The template engine to use (e.g., 'django.template.backends.django.DjangoTemplates').

* DIRS: 
A list of directories where Django should look for templates. It's common to have a project-level templates directory.

* APP_DIRS: 
A boolean indicating whether Django should look for templates in a templates folder inside each installed app.

* OPTIONS: 
Additional configuration options like context_processors (for data available to all templates) and debug.