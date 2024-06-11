from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
