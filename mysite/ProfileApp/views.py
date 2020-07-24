from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def profile_render(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('/profile/login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Success, you have been registered')
            return redirect('/profile/')

        else:
            messages.error(request, 'Sorry, you do something wrong')

    else:
        registration_form = RegistrationForm()
    context = {
        "registration_form": registration_form,
    }
    return render(request, 'authentication/registration.html', context)
