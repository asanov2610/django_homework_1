from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        info = [name, phone, message]
        with open('contacts.txt', 'a', encoding='utf-8') as file:
            for line in info:
                file.write(line + '\n')

    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'catalog/product_detail.html', context)
