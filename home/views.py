from django.shortcuts import render


def say_hello(request):
    return render(request, 'hello.html')


def index(request):
    return render(request, 'home.html')
