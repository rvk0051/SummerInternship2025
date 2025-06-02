# Installing Django and creating a project

Steps for installing Django:-

## 1. Install pip:-

    python -m pip install -U pip
## 2. Create virtual environment in your project:-
Creating virtual machine is necessary for every project as all the installations are needed to be done in that virtual machine, to install virtual machine, use the following command:- 
     
    python -m venv my_env
## 3. Activate the virtual environment:-
To use virtual environment, it is needed to be activated, which would be done by the following command:-
     
    my_env\Scripts\activate
## 4. Installing Django:-
after activating the virtual machine, install Django using the following command:-
    
    pip install django
## 5. Creating a django project:-
To make a django project, use the following command in the terminal-
    
    django-admin startproject <project_name>
## 6. Creating a django app:-
A django project can have multiple django projects, to make one, use the following command:-

    python manage.py startapp <my_app_name>

## 7. Run the Development Server:-
To run a development server, use the following command:-

    python manage.py runserver