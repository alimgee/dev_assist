from django.urls import path, include
from cart.views import view_cart, add_to_cart, delete_from_cart

urlpatterns = [
    path('', view_cart, name='view-cart'),
    path('add/<id>/', add_to_cart, name='add-to-cart'),
    path('delete/<id>/', delete_from_cart, name='delete-from-cart'),
]