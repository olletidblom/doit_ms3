from django.urls import path
from .views import taskList, taskDetail, createTask, editTask, deleteTask

urlpatterns = [
    path('', taskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create_task/', createTask.as_view(), name='create_task'),
    path('edit_task/<int:pk>/', editTask.as_view(), name='edit_task' ),
    path('delete_task/<int:pk>/', deleteTask.as_view(), name='delete_task' )
]