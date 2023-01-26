from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField

    class Meta(UserCreationForm):
        model = CustomUser

        fields = ('username', 'email', 'password1', 'password2')
