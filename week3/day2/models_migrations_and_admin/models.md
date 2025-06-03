# Django Models
In Django, models are a fundamental part of the framework that define the structure of your data. They are Python classes that represent database tables, and each attribute of the class corresponds to a field in the table. Models are a key component of Django's Object-Relational Mapping (ORM) system, which allows you to interact with the database using Python code instead of raw SQL.

1. ### Defining Models:
* Models are defined in the models.py file of your Django app. Each model class inherits from django.db.models.Model.
* Each attribute of the model class represents a database field, and you define the field types using Django's built-in field classes.

2. ### Field Types:

Django provides a variety of field types to represent different kinds of data. Some common field types include:
* CharField: A string field for short text (e.g., names).
* TextField: A field for longer text (e.g., descriptions).
* IntegerField: A field for integers.
* FloatField: A field for floating-point numbers.
* BooleanField: A field for True/False values.
* DateField: A field for date values.
* DateTimeField: A field for date and time values.
* ForeignKey: A field for creating a many-to-one relationship with another model.

3. ### Meta Class:

You can define a Meta class inside your model to provide additional options, such as the database table name, ordering, and verbose names.

4. ### Methods:

You can define methods within your model class to add custom behavior. For example, you might define a __str__ method to return a human-readable string representation of the model instance.