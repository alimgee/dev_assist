from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from forum.forms import QueryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

    
# creating community page view using functions instead
def community(request):
    querys = Post.objects.all()
    page = request.GET.get('page', 1)
    print(f' page is {page}')
    paginator = Paginator(querys, 3)
    post_pag = paginator.get_page(page)
    context = {
        
        "posts": post_pag
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
@login_required
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

@login_required
def edit_query(request, pk):
    ''' Function to allow a user to edit their own query'''
    query = get_object_or_404(Post, pk=pk)
    logged_user = request.user.id
    author = query.author.id
    if logged_user is not author:
        messages.warning(request, f'you do not own this post')
        return redirect('posts')

    if request.method == "POST":
        query_form = QueryForm(request.POST, instance=query)
        if query_form.is_valid():
            #query_form.instance.date_posted = timezone.now()
            query_form.save()
            messages.success(
                request, f"You have successfully changed your query")
            return redirect(query_detail, query.pk)
    else:
        query_form = QueryForm(instance=query)
    context = {
        "form": query_form,
    }
    return render(request, "forum/edit_form.html", context)

@login_required
def delete_query(request, pk):
    '''
    Function to allow Query owner to delete their post
    '''
    query = get_object_or_404(Post, pk=pk)
    logged_user = request.user.id
    author = query.author.id

    if logged_user is not author:
        messages.warning(request, f'You are not the current owner of this query')
        return redirect('posts')

    query.delete()
    messages.success(
        request, f"Your Post has now been removed")
    return redirect('posts')
