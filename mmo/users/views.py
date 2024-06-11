from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }

    def get_success_url(self):
        return reverse_lazy('index')
