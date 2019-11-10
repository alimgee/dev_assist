from django.urls import path
from .views import PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.community, name='posts'),
    path('query/<int:pk>/', views.query_detail, name='post-detail'),
    #path('query/new/', PostCreateView.as_view(), name='post-create'),
    path('query/new/', views.create_query, name='post-create'),
    path('query/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

]