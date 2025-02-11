from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your models here.


class Index(TemplateView):
    template_name = 'todo/index.html'

