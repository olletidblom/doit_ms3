from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


# Create your models here.


class taskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        return context


class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
    
class createTask(CreateView):
    model = Task 
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'create_task'
    template_name = 'todo/create.html'
    
class editTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'edit_task'
    template_name = 'todo/edit.html'
    
    
class deleteTask(DeleteView):
    model = Task 
    context_object_name ='task'
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('tasks')
    
