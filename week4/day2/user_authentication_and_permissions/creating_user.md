## Creating User:-
While creating user, never use raw password(A raw password is the original plain text password a user enters before any hashing or encryption is applied.), e.g.;

    User.objects.create(username='john', password='john@123')  # ❌ Dangerous!

It will be saved as plain text, which means:
* Anyone with DB access can see it
* If your DB is compromised, all user accounts are exposed
* It's a huge security risk

This should be used:-

    User.objects.create_user(username='john', password='john@123')

or

    user.set_password('john@123')

Django:
* Hashes the raw password using a secure algorithm (PBKDF2)
* Stores only the hashed version

Example of a hashed password:- pbkdf2_sha256$260000$abcXYZ...$long_hashed_string 
(this is a hashed password by Django not the one entered by the user.)


## Authentication Workflow:-
* User submits credentials
* Django checks via authenticate()
* If valid → login(request, user)
* Session is created

##### Example:-
    from django.contrib.auth import authenticate, login

    user = authenticate(username='john', password='pass1234')
* Finds the user with the given username
* Hashes the provided password using the same hash function as stored password
* Compares the hashes
* If valid → returns the user object
* If invalid → returns None


    if user:
        login(request, user)
* Creates a session for the user (stores user ID in session)
* User stays logged in as long as session exists
* You can now use request.user across views