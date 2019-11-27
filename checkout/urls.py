from django.urls import path
from checkout import views as checkout_view

urlpatterns = [
    path('', checkout_view.checkout, name='checkout'),

]
