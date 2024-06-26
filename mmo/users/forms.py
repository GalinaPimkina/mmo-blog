from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    '''форма авторизации'''

    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationUserForm(UserCreationForm):
    '''форма регистрации'''

    username = forms.CharField(label='Логин')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повтор пароля')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        '''проверка уникальности email при регистрации'''

        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Этот e-mail адрес уже зарегистрирован!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    password = forms.CharField(disabled=True, label='Пароль', widget=forms.PasswordInput())
    date_joined = forms.DateTimeField(disabled=True, label='Дата регистрации')

    class Meta:
        model = get_user_model()
        fields = ['username', 'nickname', 'avatar', 'email', 'first_name', 'last_name', 'password', 'date_joined']
        labels = {
            'nickname': 'Никнейм',
            'avatar': 'Аватар',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

class ConfirmEmailForm(forms.ModelForm):
    token = forms.CharField(max_length=6, label='Введите проверочный код')

    class Meta:
        model = get_user_model()
        fields = ['token', ]


