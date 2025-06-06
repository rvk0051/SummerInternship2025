"""
This module handles all authentication-related functionality which includes:
- User registration
- User dashboard display
- Profile editing

Key Components:
1. Dashboard View: Shows user's posts in chronological order
2. Registration View: Handles new user sign-ups
3. Profile Edit View: Manages user profile updates

Dependencies:
- Django authentication system
- Custom forms (RegisterForm, ProfileUpdateForm)
- Django messaging framework

Usage:
These views are typically connected to URLs like:
- /dashboard/
- /register/
- /profile/edit/
"""

from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import RegisterForm, ProfileUpdateForm


@login_required
def dashboard(request):
    """
    Display user's personal dashboard.

    - Shows all posts created by the user
    - Orders posts by creation date (newest first)
    - Requires user authentication
    
    Returns:
        Rendered dashboard template with user's posts
    """
    user_posts = (request.user.post_set
                 .all()
                 .order_by('-created_at'))
    
    context = {'posts': user_posts}
    return render(request, 'blogging/dashboard.html', context)


def register(request):
    """
    Handle user registration.
    
    Workflow:
    1. Display empty form for GET requests
    2. Process form data for POST requests
    3. Create new user if data is valid
    4. Log in the user automatically after registration

    Returns:
        - Successful registration: Redirects to dashboard
        - Invalid form: Returns form with error messages
    """
    if request.method != "POST":
        return render(request, 
                     "registration/register.html",
                     {"form": RegisterForm()})

    form = RegisterForm(request.POST)
    if not form.is_valid():
        return render(request, 
                     "registration/register.html",
                     {"form": form})

    try:
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect(reverse('dashboard'))
    
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Registration error: {e}")
        form.add_error(None, "Registration failed. Please try again.")
        return render(request, 
                     "registration/register.html",
                     {"form": form})


@login_required
def edit_profile(request):
    """
    Handle user profile updates.

    - Requires user authentication
    - Pre-fills form with current profile data
    - Validates and saves profile updates
    
    Workflow:
    1. GET request: Display current profile data
    2. POST request: Process profile updates
    
    Returns:
        - Successful update: Redirects to dashboard
        - Invalid form: Returns form with error messages
    """
    profile = request.user.profile

    if request.method != 'POST':
        form = ProfileUpdateForm(instance=profile)
        return render(request,
                     'blogging/edit_profile.html',
                     {'form': form})

    form = ProfileUpdateForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('dashboard')

    return render(request,
                 'blogging/edit_profile.html',
                 {'form': form})