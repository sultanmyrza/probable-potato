from django.shortcuts import render

from shop.models import Category, SubCategory, Product
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    vip_products = products.filter(importance='vip')
    context = {
        'categories': categories,
        'vip_products': vip_products,
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    context = {
        'categories': Category.objects.all(),
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'shop/product_detail.html', context)


def products_list(request, sub_category_id):
    sub_category = SubCategory.objects.get(id=sub_category_id)
    products = sub_category.product_set.all()
    context = {
        'categories': Category.objects.all(),
        'products': products,
    }
    return render(request, 'shop/products_list.html', context)


def contact_us(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'shop/contact.html', context)