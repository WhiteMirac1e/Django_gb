from django.core.management.base import BaseCommand
from myapp.models import User, Product


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'8917555357{i}',
                        adress=f'Some adress{i}')
            user.save()
            for j in range(1, count + 1):
                post = Product(name=f'Name{j}', descriptions=f'Text from {user.name} #{j} is bla bla bla many long text',
                               price=j*345, count=j)
                post.save()
