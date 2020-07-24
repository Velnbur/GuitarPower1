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
    '''
    checkbox = forms.ChoiceField(
        widget=forms.CheckboxInput(attrs={
            'class': "login-checkbox",
            'id': "f_option",
        })
    )
    '''


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=(forms.TextInput(attrs={
            "placeholder": "Enter Email",
            'class': ''
        })))
    username = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                "placeholder": "Enter Username",
                'class': ''
            })))
    first_name = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                "placeholder": "Enter Name",
                'class': ''
            })))
    last_name = forms.CharField(
        widget=(forms.TextInput(
            attrs={
                "placeholder": "Enter Surname",
                'class': ''
            })))
    password1 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                'class': ''
            })))
    password2 = forms.CharField(
        widget=(forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password Again",
                'class': ''
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
