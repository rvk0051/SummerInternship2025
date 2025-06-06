"""
Authentication Forms Module:

This module contains form classes for user authentication and profile management:
- RegisterForm: Handles new user registration with display name and password

Features:
- Custom username generation from display name
- Password validation and matching
- Automatic profile creation
- Form styling with Bootstrap classes

Dependencies:
- Django forms
- Profile model from models.py
- Django's built-in User model
"""

from django import forms
from django.contrib.auth.models import User
from ..models import Profile
import re


class RegisterForm(forms.Form):
    """
    User registration form with display name and password fields.

    Fields:
        author_name (CharField): User's display name
        password1 (CharField): Password field
        password2 (CharField): Password confirmation field

    Validation:
        - Passwords must match
        - Password length >= 8 characters
        - Unique username generation from display name
    """

    author_name = forms.CharField(
        label="Display Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your display name'
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password (minimum 8 characters)'
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )

    def clean(self):
        """
        Validate form data.

        Checks:
            1. Both passwords match
            2. Password meets minimum length requirement

        Raises:
            ValidationError: If validation fails
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    "Passwords do not match. Please enter the same password in both fields."
                )

            if len(password1) < 8:
                raise forms.ValidationError(
                    "Password must be at least 8 characters long."
                )

        return cleaned_data

    def save(self):
        """
        Create new user and associated profile.

        Process:
            1. Generate unique username from display name
            2. Create User instance
            3. Create associated Profile

        Returns:
            User: Newly created user instance
        """
        author_name = self.cleaned_data['author_name']
        password = self.cleaned_data['password1']

        # Generate base username by removing non-word characters
        base_username = re.sub(r'\W+', '', author_name.lower()) or 'user'
        username = base_username
        counter = 1

        # Ensure username uniqueness
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        # Create user and profile
        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.update_or_create(
            user=user,
            defaults={"author_name": author_name}
        )

        return user


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Fields:
        - Inherited from Profile model
        - Customized with Bootstrap styling
    """

    class Meta:
        model = Profile
        fields = ['author_name']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your display name'
            })
        }
