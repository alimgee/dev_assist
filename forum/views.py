from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create view for showing forum posts
class PostListView(ListView):
    model = Post
    template_name = 'forum/forum_list.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post 
    context_object_name = 'post'