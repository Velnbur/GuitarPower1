from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'Enter Username'}
        ),
        label='')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': '',
            'placeholder': 'Enter Password'}
        ),
        label='')
