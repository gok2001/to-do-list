from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/add-task/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/', views.show_task, name='show_task'),
    path('tasks/<int:task_id>/edit-task/', views.edit_task, name='edit_task'),
]
