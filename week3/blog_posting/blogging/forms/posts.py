"""
Profile Forms Module:

This module contains form classes for user profile management:
- ProfileUpdateForm: Form for updating user display names

- Custom field labels
- Profile model integration

Dependencies:
- Django forms
- Profile model from models.py
"""

from django import forms
from ..models import Profile


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile display names.
    
    Features:
        - Bootstrap-styled input field
        - Custom field label
        - Model-based validation
    
    Fields:
        author_name: User's display name in the system
    """
    
    class Meta:
        model = Profile
        fields = ['author_name']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'author_name': 'Display Name'
        }