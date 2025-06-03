# Django App
An app is a web application that does something specific. A project can contain multiple apps, and each app is designed to be reusable and modular. For example, you might have one app for user authentication, another for blog posts, and another for a shopping cart.
## Structure of a Django App

    myapp/
    |-  migrations/
    |-  __init__.py
    |-  admin.py
    |- apps.py
    |-  models.py
    |-  tests.py
    |-  views.py

* ##### migrations/: 
This directory contains migration files that Django uses to manage changes to your database schema.

* ##### __init__.py: 
An empty file that tells Python to treat the directory as a package.

* ##### admin.py: 
This file is where you can register your models to make them accessible in the Django admin interface.

* ##### apps.py: 
This file contains the configuration for the app itself.

* ##### models.py: 
This file is where you define your data models (database tables) using Django's ORM (Object-Relational Mapping).

* ##### tests.py: 
This file is where you can write tests for your app to ensure that it behaves as expected.

* ##### views.py: 
This file is where you define the views that handle requests and return responses.