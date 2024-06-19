# Generated by Django 5.0.6 on 2024-06-18 08:36

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название товара')),
                ('descriptions', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name=' Цена товара')),
                ('count', models.IntegerField(verbose_name='Количество товара')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('email', models.EmailField(max_length=50, verbose_name='Электронная почта клиента')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Номер телефона клиента')),
                ('adress', models.CharField(max_length=150, null=True, verbose_name='Адрес клиента')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации клиента')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цены товара')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавленяе товара')),
                ('products', models.ManyToManyField(to='myapp.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
