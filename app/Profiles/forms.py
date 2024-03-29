from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import ProfileModel


class UserLoginForm(forms.Form):

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
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': "login-checkbox",
            'id': "f_option",
        }),
        required=False
    )


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


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        fields = ('face_image',
                  'about_myself',
                  'telegram_link',
                  'facebook_link',
                  'whatsapp_link',
                  'vk_link',
                  'instagram_link',)

    face_image = forms.ImageField(widget=forms.FileInput(attrs={'class': '',
                                                                'placeholder': ''}),
                                  required=False)
    about_myself = forms.CharField(widget=forms.Textarea(attrs={'class': '',
                                                                'placeholder': '',
                                                                'value': ''}),
                                   required=False)
    telegram_link = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                                  'placeholder': 'Link for your telegram',
                                                                  'value': ''}),
                                    required=False)
    facebook_link = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                                  'placeholder': 'Link for your facebook',
                                                                  'value': ''}),
                                    required=False)
    whatsapp_link = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                                  'placeholder': 'Link for your whatsapp',
                                                                  'value': ''}),
                                    required=False)
    vk_link = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                            'placeholder': 'Link for your vk',
                                                            'value': ''}),
                              required=False)
    instagram_link = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                                   'placeholder': 'Link for your instagram',
                                                                   'value': ''}),
                                     required=False)
