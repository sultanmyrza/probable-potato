from django.shortcuts import render

from shop.models import Category, Product
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    vip_products = products.filter(importance='vip')
    context = {
        'categories': categories,
        'products': products,
        'vip_products': vip_products,
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    context = {
        'categories': Category.objects.all(),
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'shop/product_detail.html', context)


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.product_set.all()
    context = {
        'categories': Category.objects.all(),
        'products': products,
    }
    return render(request, 'shop/products.html', context)


def contact_us(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'shop/contact.html', context)