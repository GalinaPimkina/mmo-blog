from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    '''форма авторизации'''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationUserForm(UserCreationForm):
    '''форма регистрации'''

    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        '''проверка уникальности email при регистрации'''

        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This e-mail is used already!")
        return email
