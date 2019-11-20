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
    comment = Comment.query_id
    # comments = Comment.objects.all()
    comments = Comment.objects.filter(query_id = pk )
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

def edit_query(request, pk):
    ''' Function to allow a user to edit their own query'''
    query = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        query_form = Form(request.POST, instance=query)
        if query_form.is_valid():
            #query_form.instance.date_posted = timezone.now()
            query_form.save()
            messages.success(
                request, f"You have successfully changed your query")
            return redirect(query_detail, query.pk)
    else:
        query_form = QueryForm(instance=query)
    context = {
        "query_form": query_form,
    }
    return render(request, "post_form.html", context)