from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'usuario',
            'carrito',
            'fecha',
        ]
        labels = {
            'usuario' : 'Usuario',
            'carrito': 'Productos',
            'fecha' : 'Fecha de compra',
        }