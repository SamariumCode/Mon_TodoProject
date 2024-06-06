from django.shortcuts import render


def say_hello(request):
    return render(request, 'hello.html')


def index(request):
    full_name = {'name': 'Admin', 'family': 'Django', 'first': [1, 2, 3, 4], 'second': [5, 6, 7, 8]}
    return render(request, 'home.html', context={'full_name': full_name})
