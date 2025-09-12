from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms

from .models import Task


def index(request):
    task_list = Task.objects.all().order_by('-created_at')

    paginator = Paginator(task_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    
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

    context = {
            'form': forms.TaskForm(),
            'form_action': form_action,
        }

    return render(request, 'tasks/add_task.html', context)
