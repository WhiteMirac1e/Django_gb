from django import forms

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'descriptions', 'price', 'count', 'photo']