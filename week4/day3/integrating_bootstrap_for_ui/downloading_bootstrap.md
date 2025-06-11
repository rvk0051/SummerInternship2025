# Downloading Bootstrap locally

Steps for downloading Bootstrap locally and then integrating it with UI:-
##### 1. Download Bootstrap
Go to the official Bootstrap website
* Click Download
* Choose Compiled CSS and JS
* You’ll get a ZIP file — extract it.
##### 2. Place Bootstrap files in your Django static directory
```
project_root/
├── static/
│   └── bootstrap/
│       ├── css/
│       │   └── bootstrap.min.css
│       └── js/
│           └── bootstrap.bundle.min.js
```

##### 3. Load Bootstrap in your 'base.html'
in `<head>`, use this-   
`<link href="{% static 'bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">`

in `<body>`, use this-
`<script src="{% static 'bootstrap/js/bootstrap.bundle.min.js' %}"></script>`
`
##### 4. Use Bootstrap classes in your templates
Now use any Bootstrap class (like container, form-control, btn, etc.) in any template that extends this base.

### Pros of Local Method:
* Works offline.
* You can modify Bootstrap files (if needed).
* Useful for deployment in restricted environments.

### Cons of Local Method:
* Setup takes longer.
* You have to update manually when a new version comes out.