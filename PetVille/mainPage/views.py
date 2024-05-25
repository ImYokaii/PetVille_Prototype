from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, TrainingPost
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
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_posts.html' 
    context_object_name = 'posts'  
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    #template_name = 'main/home.html' redirecting
    #context_object_name = 'posts' For List View
    #ordering = ['-date_posted'] For List View

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    template_name = 'main/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    template_name = 'main/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'main/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    #template_name = 'main/home.html' redirecting
    #context_object_name = 'posts' For List View
    #ordering = ['-date_posted'] For List View

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def store(request):
    return render(request, 'main/store.html', {'title': 'Store'})

def obituary(request):
    return render(request, 'main/obituary.html', {'title': 'Obituary'})

def emergency(request):
    return render(request, 'main/emergency.html', {'title': 'Emergency'})

def training(request):
    return render(request, 'main/training.html', {'title': 'Pet Wellness'})

