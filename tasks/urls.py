from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/add_task/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/', views.show_task, name='show_task'),
    path('tasks/<int:task_id>/edit_task/', views.edit_task, name='edit_task'),
    path('tasks/completed_tasks', views.completed_tasks, name='completed_tasks'),
]
