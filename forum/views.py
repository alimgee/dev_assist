from django.shortcuts import render, reverse, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create view for showing forum posts
class PostListView(ListView):
    model = Post
    template_name = 'forum/forum_list.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
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
    success_url = '/community/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):# tests that user owns post using built in mixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return reverse('home')


def post_edit(request, pk):
    """ Edit a Single Ticket """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.instance.date_edited = timezone.now()
            ticket_form.save()
            messages.success(
                request, f"Ticket successfully updated!")
            return redirect(tickets_view_one, ticket.pk)
    else:
        ticket_form = TicketForm(instance=ticket)
    context = {
        "ticket": ticket,
        "ticket_form": ticket_form,
    }
    return render(request, "tickets_edit.html", context)