from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
