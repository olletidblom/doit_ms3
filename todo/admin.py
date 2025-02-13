from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User, Category, Task 


admin.site.register(Category)
admin.site.register(Task)