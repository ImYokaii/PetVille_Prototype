from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    postedcontent = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', postedcontent)

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
