from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('registration/done/', views.registration_done, name='registration_done'),

    path('profile/<int:pk>/', views.ProfileUserView.as_view(), name='profile'),
]