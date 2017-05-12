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
    product = Product.objects.get(id=product_id)

    categories = Category.objects.all()
    category = categories.get(id=product.category.id)
    random_products = category.product_set.all()
    print len(random_products)
    if len(random_products) > 3:
        print 'before', len(random_products)
        random_products = random_products[:3]
        print 'after ', len(random_products)
    context = {
        'categories': categories,
        'product': product,
        'suggestions': random_products,
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