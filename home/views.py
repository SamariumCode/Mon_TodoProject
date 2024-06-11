from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreateForm


def index(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'todos': all})


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, pk):
    Todo.objects.get(pk=pk).delete()
    messages.success(request, 'با موفقیت پست حذف شد', extra_tags='success')
    return redirect('index')


def create(request):

    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(
                title=cd['title'],
                description=cd['description'],
            )
            messages.success(request, 'با موفقیت ساخته شد', 'success')
            return redirect('index')
    else:

        form = TodoCreateForm()
    return render(request, 'create.html', context={'form': form})
