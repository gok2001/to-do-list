from django.shortcuts import render

from .models import Task


def index(request):
    task_list = Task.objects.all()
    context = {'tasks': task_list}
    
    return render(request, 'tasks/index.html', context)
