from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('query/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('query/new/', PostCreateView.as_view(), name='post-create'),

]