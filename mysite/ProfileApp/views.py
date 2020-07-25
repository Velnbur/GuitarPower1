from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, UserLoginForm, ProfileForm
from .models import ProfileModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate


@login_required
def profile_render(request):
    if request.method == 'POST':
        user = request.user
        profile_form = ProfileForm(request.POST, instance=user.profilemodel)
        profile = ProfileModel.objects.get(user__exact=user.id)
        if profile_form.is_valid():
            post = profile_form.save(commit=False)
            post.user = user
            post.save()
            return redirect('/profile/')
    else:
        user = request.user
        profile_form = ProfileForm(instance=user.profilemodel)
        profile = ProfileModel.objects.get(user__exact=user.id)

    context = {
        'user': user,
        'profile': profile,
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('/profile/')
    else:
        form = UserLoginForm()

    return render(request, 'authentication/login.html', {'form': form})


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
