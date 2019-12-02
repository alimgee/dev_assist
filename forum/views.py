from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from forum.models import Post, Comment
from forum.forms import QueryForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q #for multiple searchs

    
def community(request):
    ''' 
    Function to load the forum landing page
    at /community and display any current posts
    in the db
    '''
    querys = Post.objects.all()
    # adding pagination settings
    # return current page default is 1
    page = request.GET.get('page', 1)
    # setting paginator to show 3 posts
    paginator = Paginator(querys, 3)
    # passing current page to context
    post_pag = paginator.get_page(page)
    context = {
        
        "posts": post_pag
    }
    return render(request, "forum/forum_list.html", context)


def do_search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)) 
    if not posts:
        messages.warning(request, f'Your serach for "{query} " returned no results')
    context = {
        
        "posts": posts
    }
    return render(request, "forum/forum_list.html", context)


def query_detail(request, pk):
    '''
    function to show a single post detail, also
    displays any comments associated with a
    post and allows logged in users to add
    comments to post
    '''
    query_detail = get_object_or_404(Post, pk=pk)
    # getting current session user
    user = request.user
    # Creating comment form
    comment_form = CommentForm()
    # if form is submitted
    if request.method == 'POST':
        # checking user is logged in
        logged_user = request.user.id
        # dont let non logged in user add comment
        if not logged_user:
            messages.warning(request, f'You must be logged in to comment')
            return redirect('posts')
        # take submitted form
        comment_form = CommentForm(request.POST or None)
        # if submitted form is valid save it to db
        if comment_form.is_valid():         
            comment = comment_form.save(commit=False)
            # link query foregin key
            comment.query = query_detail
            # adding detail to title field
            comment.title = query_detail.title
            # adding user to foreign key field
            comment.comment_by = user
            comment.save()
            # message user and reload post detail page
            messages.success(request, f'Comment added sucessfully')
            return redirect('post-detail', pk = query_detail.pk)
    # finding comments related to current post
    comments = Comment.objects.filter(query_id = pk )
    # adding to context and returning to post detail page
    context = {
        "post": query_detail,
        "comments":comments,
        "form": comment_form

    }
    return render(request, "forum/post_detail.html", context)


@login_required
def create_query(request):
     '''
     function to create a post
     '''
     user = request.user
     # if form is submitted
     if request.method == "POST":
         # getting form
         query_form = QueryForm(request.POST)
         # if form is valid save and message
         if query_form.is_valid():
             query = query_form.save(commit=False)
             query.author = user
             query.save()
             messages.success(request, f'Thanks for submiting your ticket')
             return redirect('posts')
     else:
         # loading form for psots
         query_form = QueryForm()
     # passing form to context and loading page
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
