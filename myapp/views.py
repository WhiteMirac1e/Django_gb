import logging
from datetime import datetime, date, timedelta, timezone

from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

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
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()

            return redirect('user_products', user_id=user.id)
    else:
        product_form = ProductForm()

    context = {
        'user': user,
        'user_order_7': user_order_7,
        'user_order_30': user_order_30,
        'user_order_365': user_order_365,
        'all_product': all_product,
        'product_form': product_form,
    }
    return render(request, "myapp/user_products.html", context)




# def user_products(request, customer_id, days_history):
#     customer = get_object_or_404(User, pk=customer_id)
#     date_start = date.today() - timedelta(days=days_history)
#     products = OrderProducts.objects.select_related('product').select_related('orders').filter(
#         order__date__gte=date_start, order__customer_id=customer_id)
#     products = products.values('product__name', 'product__price').annotate(count_prod=Sum('product_count'))
#     products = products.annotate(cost=F('product__price') * F('count_prod'))
#
#     context = {
#         'client_name': customer.name,
#         'period': period(days_history),
#         'products': products
#     }
#
#     return render(request, 'myapp/user_products.html', context)
#
#
# def period(days: int) -> str:
#     """Период отчетности."""
#     match days:
#         case 7:
#             return 'за последнюю неделю'
#         case 30:
#             return 'за последний месяц'
#         case 365:
#             return 'за последний год'
#     return 'за произвольный период'
