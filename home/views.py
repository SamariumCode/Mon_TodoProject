from django.shortcuts import render
from .models import Todo


def say_hello(request):
    return render(request, 'hello.html')


def index(request):
    all = Todo.objects.all()
    return render(request, 'home.html',  context={'todos': all})
