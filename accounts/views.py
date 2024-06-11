from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import UserRegistrationForm


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
