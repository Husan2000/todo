from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import  Todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    todos = Todo.objects.filter(author=user)

    ctx = {
        'todos': todos
    }
    return render(request, 'index.html', ctx)


@login_required
def single(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)
