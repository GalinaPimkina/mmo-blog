from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegistrationUserForm


class LoginUserView(LoginView):
    '''вход в систему'''

    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }


class RegistrationUserView(CreateView):
    '''регистрация нового пользователя'''

    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {
        'title': 'Registration',
    }
    success_url = reverse_lazy('users:registration_done')


def registration_done(request):
    '''страница приветствия после регистрации'''

    return render(request, 'users/registration_done.html', {'title': 'Registration success'})
