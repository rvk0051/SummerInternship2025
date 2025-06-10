# Built-in User Roles
'is_staff' and 'is_superuser' are the built-in user roles.
These are boolean fields on the Django User model.

## 'is_staff' role:-
If `is_staff=True`, the user can access the Django admin panel.
It does NOT mean the user has all permissions — just that they’re allowed to log into the admin dashboard (/admin).
If `is_staff=False`, even if the user visits /admin, they’ll get “403 Forbidden”.

## 'is_superuser' role:-
If `is_superuser=True`, the user:
* Can log in to admin (/admin)
* Has every permission, even ones not explicitly assigned
* Can manage everything