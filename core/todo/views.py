from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import  reverse_lazy
from .models import *
# Create your views here.

class TaskList(ListView):
    model               = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model         = Task
    template_name = 'todo/task_detail.html'

class TaskCreate(CreateView):
    model       = Task
    fields      = '__all__'
    success_url = reverse_lazy('tasks')

class TaskEdit(UpdateView):
    model       = Task
    fields      = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model               = Task
    context_object_name = 'tasks'
    success_url         = reverse_lazy('tasks')
