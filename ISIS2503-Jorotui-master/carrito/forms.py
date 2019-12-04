from django import forms
from .models import Carrito

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = [
            'usuario',
            'cantidadProductos',
            'productos',
            'costoTotal',
        ]
        labels = {
            'usuario' : 'Usuario',
            'cantidadProductos': 'Cantidad de productos',
            'productos' : 'Productos',
            'costoTotal': 'Costo Total',
        }