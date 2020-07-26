from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegistrationForm, UserLoginForm, ProfileForm
from .models import ProfileModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.contrib.auth.models import User


@login_required
def profile_render(request):
    if request.method == 'POST':
        # проверка на тип http запроса

        user = request.user
        # иннициализация модели пользевателя

        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profilemodel)
        # иннициализация формы профиля
        profile = ProfileModel.objects.get(user__exact=user.id)
        # модель профиля

        if profile_form.is_valid():
            post = profile_form.save(commit=False)
            birth_date = profile_form.cleaned_data['birth_date']
            if profile.birth_date:
                post.birth_date = profile.birth_date
            elif birth_date == '':
                post.birth_date = None
            if profile.about_myself:
                post.about_myself = profile.about_myself
            post.user = user
            post.save()
            # если форма заполнена праивльно,
            # то она сохраняется в модель с соответствующим пользователем в параметре user
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
            # аутентификация пользевателя по данным параметрам из формы
            if user is not None:
                # если такой пользеватель существует,
                login(request, user)
                # происходит авторизация
                if not remember_me:
                    # если пользеваетль не поставил галочку на 'Запомнить меня'
                    request.session.set_expiry(0)
                    # выводит данные пользевателя из куки файлов
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
            user = registration_form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('authentication/email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = registration_form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'pguitarpower@gmail.com', [to_email])
            return render(request, 'authentication/check_email_template.html', {})

    else:
        registration_form = RegistrationForm()
        # иннициализация формы регистрации, при типе http запроса GET

    context = {
        "registration_form": registration_form,
    }

    return render(request, 'authentication/registration.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/profile/')
    else:
        return HttpResponse('Activation link is invalid!')
