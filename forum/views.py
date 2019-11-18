from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from forum.forms import QueryForm
from django.views.generic import  CreateView, UpdateView

    
# creating community page view using functions instead
def community(request):
    querys = Post.objects.all()
    context = {
        "posts": querys
    }
    return render(request, "forum/forum_list.html", context)

# creating query detail page view using functions instead
def query_detail(request, pk):
    query_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all()
    context = {
        "post": query_detail,
        "comments":comments,

    }
    return render(request, "forum/post_detail.html", context)

# create form to add query
def create_query(request):
     """ Create a new query """
     if request.method == "POST":
         query_form = QueryForm(request.POST)
         if query_form.is_valid():
             query_form.save()
             messages.success(request, f'Thanks for submiting your ticket')
             return redirect('posts')
     else:
         query_form = QueryForm()

     context = {
         "form": query_form,
     }
     return render(request, "forum/post_form.html", context)

