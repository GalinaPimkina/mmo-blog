from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ads.utils import DataMixin
from .forms import LoginUserForm, RegistrationUserForm, ProfileUserForm


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


class ProfileUserView(LoginRequiredMixin, DataMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Профиль пользователя')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])