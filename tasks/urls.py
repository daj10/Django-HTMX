from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.task_home, name='task-home'),
    path('add-collection/', views.add_collection, name='add-collection'),
    path('add-task/', views.add_task, name='add-task'),
    path('delete-task/<int:task_pk>/', views.delete_task, name='delete-task'),
    path('delete-collection/<int:collection_pk>/', views.delete_collection, name='delete-collection'),
    path('get-tasks/<int:collection_pk>/', views.get_tasks, name="get-tasks")
]
