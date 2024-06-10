from django.shortcuts import render
from .models import Todo


def say_hello(request):
    return render(request, 'hello.html')


def index(request):
    all = Todo.objects.all()
    return render(request, 'home.html',  context={'todos': all})


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'detail.html', context={'todo': todo})
