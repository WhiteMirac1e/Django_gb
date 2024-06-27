import logging
from datetime import datetime, timedelta
from django.shortcuts import render, redirect

from myapp.forms import ProductForm
from myapp.models import User, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return render(request, "myapp/index.html")


def about(request):
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return render(request, "myapp/about.html")


def user_products(request, user_id):
    user = User.objects.get(pk=user_id)

    last_7_days = datetime.now() - timedelta(days=7)
    user_order_7 = Product.objects.filter(order__customer=user, order__date__gte=last_7_days).distinct()

    last_30_days = datetime.now() - timedelta(days=30)
    user_order_30 = Product.objects.filter(order__customer=user, order__date__gte=last_30_days).distinct()

    last_365_days = datetime.now() - timedelta(days=365)
    user_order_365 = Product.objects.filter(order__customer=user, order__date__gte=last_365_days).distinct()

    all_product = Product.objects.all()

    if request.method == 'POST':
        return redirect('upload_image', user_id=user.id)

    context = {
        'user': user,
        'user_order_7': user_order_7,
        'user_order_30': user_order_30,
        'user_order_365': user_order_365,
        'all_product': all_product,
    }
    return render(request, "myapp/user_products.html", context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ProductForm()

    data = {
        'title': 'Добавление товара',
        'form': form,
    }
    return render(request, 'myapp/upload_image.html', data)


def show_product(request, user_id):
    orders = Order.objects.filter(customer__id=user_id)
    user = User.objects.get(pk=user_id)
    all_products = Product.objects.all()
    context = {
        'orders': orders,
        'user': user,
        'all_products': all_products,
    }
    return render(request, 'myapp/show_products.html', context)
