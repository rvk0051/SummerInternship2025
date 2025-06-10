# Permissions
A permission in Django controls whether a user can perform a certain action — like adding, deleting, or updating a model instance.
Each permission has:
* a codename (e.g. 'add_user')
* a name (e.g. 'Can add user')
* a target model (e.g. User model)

### Default Permissions in Django:-
When you define a model in your Django application and include django.contrib.auth in your INSTALLED_APPS, Django automatically creates four default permissions for each model:

1. **add_<model_name>:** 
Allows a user to add new instances of that model.
Example: 
myapp.add_book (for a Book model in myapp)

2. **change_<model_name>:** 
Allows a user to modify existing instances of that model.
Example:
myapp.change_book

3. **delete_<model_name>:** 
Allows a user to delete instances of that model.
Example: 
myapp.delete_book

4. **view_<model_name>:** 
Allows a user to view instances of that model.
Example: 
myapp.view_book

These permissions are typically checked in the Django admin interface to control who can perform CRUD (Create, Read, Update, Delete) operations on models.

### Permissions are stored in:-
These permissions are stored in the auth_permission table of the database.
Every permission is linked to:
* A model
* An app
* A codename

## Custom Permissions:-
We can also add permissions, understand by example,
  
    class Book(models.Model):
        title = models.CharField(max_length=100)

        class Meta:
            permissions = [
                ('can_publish', 'Can publish book'),
                ('can_feature', 'Can mark book as featured'),
            ]

Now, 'can_publish' and 'can_feature' are added to 'auth_permission' and can now be assigned to users or groups.

## Assigning permissions to user:-
Users can be assigned permissions through admin panel and use command in shell for example:-
  
to add:-

    from django.contrib.auth.models import User, Permission
    user = User.objects.get(username='john')
    permission = Permission.objects.get(codename='can_publish')
    user.user_permissions.add(permission)

to remove:-

    user.user_permissions.remove(permission)

## Assigning permissions to groups (user roles):-

Similar to assigning permissions to user, while assigning permissions to groups also either we use admin panel or we use command in shell:-
##### Example:-

    from django.contrib.auth.models import Group, Permission, User

    # create group
    editors = Group.objects.create(name='Editors')

    # assign permission
    perm = Permission.objects.get(codename='can_publish')
    editors.permissions.add(perm)

    # assign user to group
    user = User.objects.get(username='admin')
    user.groups.add(editors)
