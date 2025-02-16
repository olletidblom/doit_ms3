from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'category']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # If a new category is provided, create it.
        new_category = self.cleaned_data.get('new_category')
        if new_category:
            category, created = Category.objects.get_or_create(name=new_category, user=instance.user)
            instance.category = category

        if commit:
            instance.save()
        return instance
    
    
# forms.py

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']