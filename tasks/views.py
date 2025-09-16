from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import forms

from .models import Task


def index(request):
    task_list = Task.objects.filter(completed=False).order_by('-created_at')

    paginator = Paginator(task_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'site_title': 'Home - '}

    return render(request, 'tasks/index.html', context)


def show_task(request, task_id):
    single_task = get_object_or_404(Task, pk=task_id)
    site_title = f'Task {single_task.id} - '

    context = {'single_task': single_task, 'site_title': site_title}

    return render(request, 'tasks/task.html', context)


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

        return render(request, 'tasks/add_task.html', context)

    context = {
        'form': forms.TaskForm(),
        'form_action': form_action,
        'site_title': 'Add Task - ',
        'is_edit': False
    }

    return render(request, 'tasks/add_task.html', context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form_action = reverse('tasks:edit_task', args=(task_id,))

    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('tasks:show_task', task_id)

        return render(request, 'tasks/add_task.html', context)

    context = {
        'form': forms.TaskForm(instance=task),
        'form_action': form_action,
        'site_title': 'Edit Task - ',
        'is_edit': True
    }

    return render(request, 'tasks/add_task.html', context)


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    task.completed = True
    task.save()

    return redirect('tasks:index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    return redirect('tasks:index')


def completed_tasks(request):
    task_list = Task.objects.filter(completed=True).order_by('-updated_at')

    paginator = Paginator(task_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'site_title': 'Completed Tasks - '}

    return render(request, 'tasks/completed_tasks.html', context)
