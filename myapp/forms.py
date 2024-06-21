from django import forms

from myapp.models import Product


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'descriptions', 'price', 'count', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'descriptions': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }