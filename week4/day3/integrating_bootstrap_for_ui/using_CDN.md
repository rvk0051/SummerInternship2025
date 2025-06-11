# Using CDN
What is a CDN?

CDN stands for Content Delivery Network.
It's a network of servers located around the world that delivers content (like CSS, JS, images, etc.) quickly to users based on their location.

Steps for using CDN and integrating Bootstrap in UI:-
##### 1. Open your base.html template
This is the file from which all your other templates will inherit.
##### 2. Add Bootstrap CSS & JS CDNs inside <head> and before </body>

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}My Site{% endblock %}</title>

  <!-- Bootstrap CSS via CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  {% block extra_css %}{% endblock %}
</head>
<body>

  {% block content %}{% endblock %}

  <!-- Bootstrap Bundle JS (includes Popper) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

  {% block extra_js %}{% endblock %}
</body>
</html>
```
##### 3. Use Bootstrap classes in your templates
Now use any Bootstrap class (like container, form-control, btn, etc.) in any template that extends this base.

### Pros of CDN:
* Quick to set up.
* Automatically gets the latest version.
* No local storage or setup required.

### Cons of CDN:
* Needs internet connection.
* No deep customization possible (unless overriding with your own CSS).

