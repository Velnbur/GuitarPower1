from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegistrationForm, UserLoginForm, ProfileForm
from .models import ProfileModel
from Articles.models import  ArticleModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.contrib.auth.models import User


@login_required
def profile_render(request):
    # иннициализация модели пользователя
    user = request.user

    # модель профиля
    profile = ProfileModel.objects.get(user__exact=user.id)

    # инициализация самой статьи
    articles = ArticleModel.objects.all().filter(author__exact=profile.user)

    for i in articles:
        i.text = strip_tags(i.text)

    context = {
        'user': user,
        'profile': profile,
        'my_articles': articles,
        'count': articles.count(),
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
            # аутентификация пользователя по данным параметрам из формы

            if user is not None:
                # если такой пользователь существует,
                login(request, user)
                # происходит авторизация

                if not remember_me:
                    # если пользоваетль не поставил галочку на 'Запомнить меня'
                    request.session.set_expiry(0)
                    # выводит данные пользователя из куки файлов
                return redirect('/profile/')
    else:
        form = UserLoginForm()

    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # функция разлогинивания пользователя
    return redirect('/profile/login')


def register_view(request):
    if request.user.is_authenticated:
        # проверка на аутентификатор пользователя

        return redirect('/profile/')
        # если пользователь уже ввошел в аккаунт или уже зарегистрирован, то перекидывает на страничку профиля

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


def change_profile(request):
    user = request.user
    profile = ProfileModel.objects.get(user__exact=user.id)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            post = profile_form.save(commit=False)
            post.user = user
            post.save()
            return redirect('/profile/')
    else:
        profile_form = ProfileForm()
        profile_form.fields['about_myself'].widget.attrs['value'] = profile.about_myself
        profile_form.fields['telegram_link'].widget.attrs['value'] = profile.telegram_link
        profile_form.fields['facebook_link'].widget.attrs['value'] = profile.facebook_link
        profile_form.fields['whatsapp_link'].widget.attrs['value'] = profile.whatsapp_link
        profile_form.fields['vk_link'].widget.attrs['value'] = profile.vk_link
        profile_form.fields['instagram_link'].widget.attrs['value'] = profile.instagram_link

    context = {
        'profile_form': profile_form,
        'user': user,
        'profile': profile,
    }

    return render(request, "settings.html", context)
