from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    all = Todo.objects.all()
    return render(request, 'home.html',  context={'todos': all})


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('index')
