from django.urls import path
from .views import taskList, taskDetail

urlpatterns = [
    path('', taskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task') 
]