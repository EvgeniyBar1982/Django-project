from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#from django.http import HttpResponse


# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', context= {'post': post})

def detail(request,pk):
    news = Post.objects.get(pk__iexact=pk)
    return render(request, 'detail.html', context={'news':news})



