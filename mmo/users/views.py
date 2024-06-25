import random

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from ads.models import User
from ads.utils import DataMixin
from .forms import LoginUserForm, RegistrationUserForm, ProfileUserForm, ConfirmEmailForm


class LoginUserView(LoginView):
    '''вход в систему'''

    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }


class RegistrationUserView(DataMixin, CreateView):
    '''регистрация нового пользователя с присвоением ему токена'''

    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:registration_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Регистрация')

    def form_valid(self, form):
        '''присвоение юзеру токена и отправка на почту'''

        user = form.save(commit=False)
        token = random.randint(100000, 999999)
        user.token = token
        user.is_active = False
        user.save()

        send_mail(
            'Подтвердите свой электронный адрес',
            f'Код активации: {user.token}',
            'service.mmoblog@gmail.com',
            [user.email],
            fail_silently=False,
        )

        return redirect('users:confirm_email', pk=user.pk) # после отправки токена переход на страницу подтверждения


class ConfirmEmailView(DataMixin, UpdateView):
    '''страница ввода и проверки токена'''

    model = User
    form_class = ConfirmEmailForm
    template_name = 'users/confirm_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Подтверждение e-mail адреса',)

    def post(self, request, *args, **kwargs):
        if 'token' in request.POST: # если токен есть в коллекции пост
            token = request.POST['token']
            user = User.objects.filter(token=token) # ищу юзера по совпадению токена
            user_for_group = User.objects.get(token=token) # получение конкретного юзера
            if user.exists(): # если queryset содержит запись
                user.update(is_active=True) # меняю статус на активный
                user_for_group.groups.add(3) # при регистрации юзер автоматически получает группу "default_user"
                user.update(token=None) # обнуление токена, чтоб не было совпадений при последующих регистрациях
            else:
                return render(request, 'users/confirm_failed.html', {'title': 'Подтверждение не удалось', 'pk': self.kwargs['pk']}) #если токен введен с ошибкой

        return render(request, 'users/confirm_success.html', {'title': 'Почта подтверждена'}) #если токен введен верно


class ProfileUserView(LoginRequiredMixin, DataMixin, UpdateView):
    '''страница профиля пользователя, его можно редактировать'''

    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Профиль пользователя {self.request.user.nickname}')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])