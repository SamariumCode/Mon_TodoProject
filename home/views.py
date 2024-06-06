from django.shortcuts import render
from .models import Todo


def say_hello(request):
    all = Todo.objects.all()
    return render(request, 'hello.html', context={'all': all})


def index(request):
    full_name = {'name': 'Admin', 'family': 'Django', 'first': [1, 2, 3, 4], 'second': [5, 6, 7, 8]}
    return render(request, 'home.html', context={'full_name': full_name})
