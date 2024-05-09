from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='mainPage-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='mainPage-about'),
]