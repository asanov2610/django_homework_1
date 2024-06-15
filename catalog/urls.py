from django.urls import path

from catalog.views import ContactPageView, ProductListView, ProductDetailView

urlpatterns = [
    path('contacts/', ContactPageView.as_view(template_name='catalog/contacts.html'), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]