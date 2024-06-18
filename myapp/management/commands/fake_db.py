from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            order = Order(customer=f'Name{i}', products=f'mail{i}@mail.ru', all_price=i*543)
            order.save()
            for j in range(1, count + 1):
                product = Product(name=f'Name{j}', descriptions=f'Text from {user.name} #{j} is bla bla bla many long text',
                               price=j*345, count=j)
                product.save()
