from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField

    class Meta(UserCreationForm):
        model = CustomUser

        fields = ('username', 'email', 'password1', 'password2')

class UserChangeIconForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser

        fields = ('icon', )


class UserChangeUsernameForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser

        fields = ('icon',)



