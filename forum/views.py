from django.shortcuts import render, reverse, get_object_or_404
from .models import Post, Comment
from forum.forms import QueryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
     else:
         query_form = QueryForm()

     context = {
         "form": query_form,
     }
     return render(request, "forum/post_form.html", context)


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