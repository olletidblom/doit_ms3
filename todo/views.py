from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.contrib import messages



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
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f"Task '{form.instance.title}' created successfully!")
        return response
    
    
    
class editTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    context_object_name = 'edit_task'
    template_name = 'todo/edit.html'

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            messages.error(self.request, "You are not allowed to edit this task.")
            return redirect('tasks')  # Prevents unauthorized edits
        response = super().form_valid(form)
        messages.success(self.request, f"Task '{form.instance.title}' edited successfully!")
        return response
    
    
class deleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('tasks')

    def post(self, request, *args, **kwargs):
        """Handle the delete request with CSRF protection"""
        task = self.get_object()

        # Prevent unauthorized deletes
        if task.user != request.user:
            messages.error(self.request, "You are not allowed to delete this task.")
            return redirect('tasks')

        # Add a success message
        messages.success(self.request, f"Task '{task.title}' deleted successfully!")

        # Delete the task and redirect
        return super().post(request, *args, **kwargs)

class createCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('categorys')  # Redirect after creating a category
    template_name = 'todo/create_category.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign user
        response = super().form_valid(form)
        messages.success(self.request, f"Category '{form.instance.name}' created successfully!")  # ✅ Use `name`
        return response

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['error_message'] = "Please correct the errors below."
        return self.render_to_response(context)
    
    
class deleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'todo/delete_category.html'  # Create this template
    success_url = reverse_lazy('categorys')  # Redirect to task list after deleting

    def get_queryset(self):
        # Ensure users can only delete their own categories
        return Category.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        messages.success(self.request, f"Category '{category.name}' deleted successfully!")
        return super().delete(request, *args, **kwargs)
    

class categoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'  # This is how you'll access categories in the template
    template_name = 'todo/category.html'  # Make sure you create this template

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)    
    
    
class editCategory(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']  # ✅ Ensure you're using the correct field
    context_object_name = 'edit_category'
    template_name = 'todo/edit_category.html'
    success_url = reverse_lazy('categorys')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f"Category '{form.instance.name}' edited successfully!")  # ✅ Use `name`, not `title`
        return response
    
        
        
class DeleteFinishedTasks(LoginRequiredMixin, View):
    
    
    def post(self, request):
        deleted_count, _ = Task.objects.filter(user=request.user, completed=True).delete()
        if deleted_count > 0:
            messages.success(self.request, f"Deleted {deleted_count} completed tasks.")
        else:
            messages.info(self.request, "No completed tasks to delete.")
        return redirect('tasks')