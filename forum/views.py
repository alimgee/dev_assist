from django.shortcuts import render
from .models import Post, Comment
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

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        comments = "here it goes"
        context["comments"] = Comment.objects.all()
        #context["posts"] = Post.objects.filter(post_id=Post.pk)
        return context