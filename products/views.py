from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views import generic, View


def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/product_detail.html', {'product': product})
