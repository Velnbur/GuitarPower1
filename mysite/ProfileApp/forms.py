from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'login-input',
            'placeholder': 'Логин',
            'onfocus': 'this.placeholder=""',
            'onblur': 'this.placeholder="Логин"'
        }),
        label='')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login-input',
            'placeholder': 'Пароль',
            'onfocus': 'this.placeholder=""',
            'onblur': 'this.placeholder="Пароль"'
        }),
        label='')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=(forms.TextInput(attrs={
            'class': 'registration-input',
            'placeholder': 'Email',
            'onfocus': 'this.placeholder=""',
            'onblur': 'this.placeholder="Email"'
        })))
    username = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                'class': 'registration-input',
                'placeholder': 'Логин',
                'onfocus': 'this.placeholder=""',
                'onblur': 'this.placeholder="Логин"'
            })))
    first_name = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                'class': 'registration-input',
                'placeholder': 'Имя',
                'onfocus': 'this.placeholder=""',
                'onblur': 'this.placeholder="Имя"'
            })))
    last_name = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                'class': 'registration-input',
                'placeholder': 'Фамилия',
                'onfocus': 'this.placeholder=""',
                'onblur': 'this.placeholder="Фамилия"'
            })))
    password1 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={
                'class': 'registration-input',
                'placeholder': 'Пароль',
                'onfocus': 'this.placeholder=""',
                'onblur': 'this.placeholder="Пароль"'
            })))
    password2 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={
                'class': 'registration-input',
                'placeholder': 'Введите пароль ещё раз',
                'onfocus': 'this.placeholder=""',
                'onblur': 'this.placeholder="Введите пароль ещё раз"'
            })))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user
