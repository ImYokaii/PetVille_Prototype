from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.

def home(request):
    postedcontent = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', postedcontent)

class PostListView(ListView):
    model = Post
    template_name = 'main/home.html' 
    context_object_name = 'posts' 
    ordering = ['-date_posted'] 

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    #template_name = 'main/home.html' redirecting
    #context_object_name = 'posts' For List View
    #ordering = ['-date_posted'] For List View

class PostCreateView(CreateView):
    model = Post 
    fields = ['title', 'content']

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
