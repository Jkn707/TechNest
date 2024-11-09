from django.shortcuts import render
from product.models import Product
from django.utils.translation import gettext as _

def home_view(request):
    if request.method == 'GET':
        filter = request.GET.get('filter')
        if filter:
            products = Product.objects.filter(name__icontains=filter)
            return render(request, 'home.html', {'products': products, 'filter': filter})
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})
