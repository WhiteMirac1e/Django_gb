from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта клиента')
    phone = PhoneNumberField(null=True, verbose_name='Номер телефона клиента')
    adress = models.CharField(null=True, max_length=150, verbose_name='Адрес клиента')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации клиента')

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, adress: {self.adress}, date: {self.date}'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название товара')
    descriptions = models.TextField(null=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Цена товара')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')
    photo = models.ImageField(upload_to='products_photo/', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return f'Name is {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    all_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)],
                                   verbose_name='Цены товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_count = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.order.primary_key}. {self.product.name} - {self.product_count}'
