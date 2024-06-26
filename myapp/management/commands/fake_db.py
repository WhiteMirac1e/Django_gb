import random

from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order, OrderProducts
from datetime import datetime, timedelta

# максимум продуктов в заказе
MAX_PROD_IN_ORDER = 10

# максимум продуктов в наличии
MAX_PRODUCTS = 100

# Кол-во генерируемых записей в таблицах
DEFAULT_CLIENTS = 10
DEFAULT_PRODUCTS = 10
DEFAULT_ORDERS = 10

# Ценовой диапазон продуктов
MIN_PRICE = 100
MAX_PRICE = 1000


class Command(BaseCommand):
    help = f"Заполнение базы тестовыми данными. Количество продукта в заказе от 1 до {MAX_PROD_IN_ORDER} включительно"

    def add_arguments(self, parser):
        parser.add_argument("-c", "--clients", type=int,
                            help=f'Count of clients for generate. {DEFAULT_CLIENTS} on default.')
        parser.add_argument("-p", "--products", type=int,
                            help=f'Count of products for generate. {DEFAULT_PRODUCTS} on default.')
        parser.add_argument("-o", "--orders", type=int,
                            help=f'Count of orders for generate. {DEFAULT_ORDERS} on default per user.')

    def handle(self, *args, **options):
        clients_count = DEFAULT_CLIENTS if options['clients'] is None else options['clients']
        products_count = DEFAULT_PRODUCTS if options['products'] is None else options['products']
        orders_count = DEFAULT_ORDERS if options['orders'] is None else options['orders']

        # генерация клиентов
        customers = [
            User(name=f'Client_{x}', email=f'client{x}@mail.ru', phone=None, adress=None)
            for x in range(1, clients_count + 1)]
        for customer in customers:
            customer.save()

        # генерация продуктов
        products = [Product(name=f'Product {x}', descriptions=None, price=random.randint(MIN_PRICE, MAX_PRICE),
                            count=random.randint(1, MAX_PRODUCTS))
                    for x in range(1, products_count + 1)]
        for prod in products:
            prod.save()

        # генерация заказов
        orders = list()
        for customer in customers:
            for _ in range(orders_count):
                order = Order.objects.create(customer=customer)
                orders.append(order)

        # заполнение заказов продуктами
        start = datetime.strptime('01.01.2023', '%d.%m.%Y')
        end = datetime.strptime('01.01.2024', '%d.%m.%Y')

        for order in orders:
            prod_in_order = random.randint(1, products_count)
            order.order_date = self.get_random_date(start, end)
            for _ in range(prod_in_order):
                prod = random.choice(products)
                # if OrderProducts.objects.filter(order_id=order.pk, product_id=prod.pk).first() is None:
                prod_cnt = random.randint(1, MAX_PROD_IN_ORDER)
                OrderProducts.objects.create(order=order, product=prod, product_count=prod_cnt)
                order.all_price += prod_cnt * prod.price
            order.save()

        self.stdout.write('Test data was created.')

    def get_random_date(self, start, end):
        delta = end - start
        return start + timedelta(random.randint(0, delta.days))
