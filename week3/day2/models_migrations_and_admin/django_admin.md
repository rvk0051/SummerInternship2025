# Django Admin
Django provides a powerful and customizable admin interface that allows you to manage your application's data easily. The Django admin is automatically generated based on your models, making it a convenient tool for performing CRUD (Create, Read, Update, Delete) operations on your data without writing any additional code.

### Key Features of Django Admin:-

#### 1. Automatic Interface Generation:

When you register your models with the admin site, Django automatically generates a user-friendly interface for managing those models.

#### 2. Customizable:

You can customize the admin interface to suit your needs, including changing the layout, adding filters, and defining how data is displayed.

#### 3. User Authentication:

The admin interface is protected by Django's authentication system, allowing you to manage user permissions and access control.

#### 4. Search and Filtering:

The admin interface provides built-in search and filtering capabilities, making it easy to find specific records.

#### 5. Inline Editing:

You can edit related models inline, allowing for a more efficient data management experience.

## Accessing Djnago Admin:-

#### 1. Run the Development Server:
   
    python manage.py runserver

#### 2. Access the Admin Interface: 
Open your web browser and go to http://127.0.0.1:8000/admin/.

#### 3. Log In: 
To login on admin interface, it is needed to have a superuser account, run the below command in the terminal to create superuser and set user_id and password of admin.
    
    python manage.py createsuperuser
