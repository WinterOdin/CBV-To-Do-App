from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  FormView, CreateView, DeleteView, UpdateView
from django.urls import  reverse_lazy
from .models import *

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomRegister(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(CustomRegister, self).form_valid(form)

class CustomLogin(LoginView):
    fields      = ['title','description','complete']
    redirect_authenticated_user = True
    template_name = 'todo/login.html'


    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin
,ListView):
    model               = Task
    context_object_name = 'tasks'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin
,DetailView):
    model         = Task
    template_name = 'todo/task_detail.html'

class TaskCreate(LoginRequiredMixin
,CreateView):
    model       = Task
    fields      = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskEdit(LoginRequiredMixin,
UpdateView):
    model       = Task
    fields      = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin
,DeleteView):
    model               = Task
    context_object_name = 'tasks'
    success_url         = reverse_lazy('tasks')
