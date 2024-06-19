from django.contrib import admin
from .models import User, Product, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adress', 'date']
    list_filter = ['date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'price', 'date', 'photo']
    list_filter = ['date', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта (name)'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'all_price', 'date']
    list_filter = ['date']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
