from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    context = {
        'title': 'Store',
    }

    return render(request, 'products/index.html', context=context)


def product(request, category_id=None, page=1):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)

    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({
        "products": products_paginator
    })

    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать!',
        'user_name': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ],
    }

    return render(request, 'products/test_context.html', context=context)
