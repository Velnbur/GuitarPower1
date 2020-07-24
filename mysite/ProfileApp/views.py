from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def profile_render(request):
    user = request.user
    # иннициализация модели пользователя

    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    # функция разлогинивания пользевателя
    return redirect('/profile/login')


def register_view(request):
    if request.user.is_authenticated:
        # проверка на аутентификатор пользевателя

        return redirect('/profile/')
        # если пользеватель уже ввошел в аккаунт или уже зарегистрирован, то перекидывает на страничку профиля

    if request.method == "POST":
        # проверка на тип http запроса

        registration_form = RegistrationForm(request.POST)
        # иннициализация формы регистрации, при типе http запроса POST

        if registration_form.is_valid():
            # проверка на правильность заполнения формы

            registration_form.save()
            # сохранение формы регистрации пользевателя

            return redirect('/profile/')
            # при успешности аперации, перекидывает на страничку профиля

    else:
        registration_form = RegistrationForm()
        # иннициализация формы регистрации, при типе http запроса GET

    context = {
        "registration_form": registration_form,
    }

    return render(request, 'authentication/registration.html', context)

'''
class CheckBoxLoginView(auth_views.LoginView):
    template_name = "authentication/login.html"
    authentication_form = UserLoginForm

    if authentication_form.check_test:
        set_expiry()
'''
