from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView

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
        context["comments"] = Comment.objects.all()
        
        
        return context
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)