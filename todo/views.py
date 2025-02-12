from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Task
# Create your models here.


class taskList(ListView):
    model = Task
    context_object_name = 'tasks'
    


class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
    