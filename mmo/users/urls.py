from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),#авторизация
    path('logout/', LogoutView.as_view(), name='logout'),#выход из системы

    path('registration/', views.RegistrationUserView.as_view(), name='registration'),#регистрация
    path('registration/confirm_email/<int:pk>/', views.ConfirmEmailView.as_view(), name='confirm_email'),#подтверждение почты

    path('profile/<int:pk>/', views.ProfileUserView.as_view(), name='profile'), #профиль пользователя
]