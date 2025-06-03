# Migrations in Django
In Django, migrations are a way to manage changes to your database schema over time. They allow you to create, modify, and delete database tables and fields in a systematic and version-controlled manner. Migrations are an essential part of Django's Object-Relational Mapping (ORM) system, enabling you to keep your database schema in sync with your models.
## 1. Migration Files:
Migrations are represented as Python files that contain a series of operations to be applied to the database. Each migration file is timestamped and named according to the changes it represents.
Migration files are stored in the migrations directory of your app.
## 2. Creating Migrations:

When you make changes to your models (e.g., adding a new field, modifying an existing field, or creating a new model), you need to create a migration to reflect those changes in the database.

You can create a migration by running the following command:

    python manage.py makemigrations
This command analyzes your models and generates a new migration file in the migrations directory.
## 3. Applying Migrations:

Once you have created a migration, you need to apply it to the database to update the schema. You can do this by running:

    python manage.py migrate
This command applies all unapplied migrations in the correct order, ensuring that your database schema matches your models.

## 4. Migration Operations:

Migrations can include various operations, such as:
* CreateModel: Create a new database table for a model.
* AddField: Add a new field to an existing table.
* RemoveField: Remove a field from a table.
* AlterField: Change the attributes of an existing field (e.g., changing its type or constraints).
* DeleteModel: Delete a database table for a model.

## 5. Migration History:

Django keeps track of which migrations have been applied to the database in a special table called django_migrations. This allows Django to know which migrations need to be applied or rolled back.

## 6. Rolling Back Migrations:

If you need to undo a migration, you can use the migrate command with the migration name you want to roll back to.
       
     python manage.py migrate <app_name> <migration_name>