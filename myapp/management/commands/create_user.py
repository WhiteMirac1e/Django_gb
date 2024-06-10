from django.core.management.base import BaseCommand

from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', phone=8 - 800 - 555 - 55 - 55, adress='Moscow')
        user.save()
        self.stdout.write(f'{user}')
