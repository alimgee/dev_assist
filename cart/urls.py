from django.urls import path, include
from cart.views import view_cart, add_to_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<pk>/', add_to_cart, name='add_to_cart'),
]