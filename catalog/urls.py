from django.urls import path

from catalog.views import contacts, product_list, product_detail

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', product_list, name='product_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
]