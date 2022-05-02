from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    """Customize form that create User"""
    email = forms.EmailField(max_length=254, help_text="Obligatoire")
    username = forms.CharField(max_length=60, help_text="Obligatoire")

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
