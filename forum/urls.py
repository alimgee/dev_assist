from django.urls import path
from .views import PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='posts'),
    path('', views.community, name='posts'),
    #path('query/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('query/<int:pk>/', views.query_detail, name='post-detail'),
    path('query/new/', PostCreateView.as_view(), name='post-create'),
    path('query/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

]