from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Category
from .forms import TaskForm, CategoryForm


# Create your models here.


class taskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        
        return context


class taskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
    
class createTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm  # Use the updated custom form
    success_url = reverse_lazy('tasks')
    template_name = 'todo/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user to the task
        return super().form_valid(form)
    
class editTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'edit_task'
    template_name = 'todo/edit.html'
    
    
class deleteTask(LoginRequiredMixin, DeleteView):
    model = Task 
    context_object_name ='task'
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('tasks')
    


class createCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category')  # Redirect to task list after creating a category
    template_name = 'todo/create_category.html'  # Create this template file

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user to the category
        return super().form_valid(form)
    
class deleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'todo/delete_category.html'  # Create this template
    success_url = reverse_lazy('tasks')  # Redirect to task list after deleting

    def get_queryset(self):
        # Ensure users can only delete their own categories
        return Category.objects.filter(user=self.request.user)
    

class categoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'  # This is how you'll access categories in the template
    template_name = 'todo/category.html'  # Make sure you create this template

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)    
    
    
class editCategory(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    
    context_object_name = 'edit_category'
    template_name = 'todo/edit_category.html'
        