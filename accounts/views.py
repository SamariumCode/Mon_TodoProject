from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import UserRegistrationForm, UserLoginForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
            )

            messages.success(
                request, 'کاربر جدید با موفقیت ساخته شد', extra_tags='success')
            return redirect('index')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'کاربر گرامی شما با موفقیت وارد شدید', extra_tags='success')
                return redirect('index')
            else:
                messages.error(
                    request, 'نام کاربری یا رمز عبور شما اشتباه هست', extra_tags='danger')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(
        request, 'کاربر گرامی شما با موفقیت خارج شدید', extra_tags='success')
    return redirect('index')
