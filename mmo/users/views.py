from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import LoginUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }

