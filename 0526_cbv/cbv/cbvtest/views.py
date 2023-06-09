from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# Create your views here.
class BlogView(ListView):
    model = ClassBlog
class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title','body']
    success_url = reverse_lazy('list')
class BlogDetail(DetailView):
    model = ClassBlog
class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title','body']
    success_url = reverse_lazy('list')
class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')