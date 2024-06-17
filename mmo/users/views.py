from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from ads.models import User
from ads.utils import DataMixin
from .forms import LoginUserForm, RegistrationUserForm, ProfileUserForm


class LoginUserView(LoginView):
    '''вход в систему'''

    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }


class RegistrationUserView(DataMixin, CreateView):
    '''регистрация нового пользователя'''

    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:registration_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Регистрация')


def registration_done(request):
    '''страница приветствия после регистрации'''

    return render(request, 'users/registration_done.html', {'title': 'Регистрация успешна'})

#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.is_active = False
#         user.save()

class ProfileUserView(LoginRequiredMixin, DataMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Профиль пользователя {self.request.user.nickname}')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])