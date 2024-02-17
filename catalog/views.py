from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'catalog/home_page.html')

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