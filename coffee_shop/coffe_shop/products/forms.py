from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo", "stock"]
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "price": "Precio",
            "available": "Disponible",
            "photo": "Foto",
            "stock": "Stock",
        }
