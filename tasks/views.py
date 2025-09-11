from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms

from .models import Task


def index(request):
    task_list = Task.objects.all()
    context = {'tasks': task_list}
    
    return render(request, 'tasks/index.html', context)


def add_task(request):
    form_action = reverse('tasks:add_task')

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    # else:
    #     form = forms.TaskForm()

    context = {
            'form': forms.TaskForm(),
            'form_action': form_action,
        }

    return render(request, 'tasks/add_task.html', context)
