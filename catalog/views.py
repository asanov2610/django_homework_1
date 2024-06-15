from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product


class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product

