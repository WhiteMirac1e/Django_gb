from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта клиента')
    phone = models.IntegerField(verbose_name='Номер телефона клиента')
    adress = models.CharField(max_length=150, verbose_name='Адрес клиента')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации клиента')

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, adress: {self.adress}, date: {self.date}'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название товара')
    descriptions = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=' Цена товара')
    count = models.IntegerField(verbose_name='Количество товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    all_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цены товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')
