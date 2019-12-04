from django.db import models
from ..variables.models import Variable
from ..usuarios.models import Usuario

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete=models.CASCADE, default=None)
    cantidadProductos = models.IntegerField()
    productos = [models.ForeignKey(Variable, null = False, blank = False, on_delete=models.CASCADE, default=None)]
    costoTotal = models.CharField(max_length=50)


def __str__(self):
    detallesCarrito = []
    i = 0
    while i<len(self.productos):
        detallesCarrito[i] = "Nombre producto: "+self.productos[i].name +" Cantidad: "+self.productos[i].cantidad
        i = i+1

    return '{}'.format(detallesCarrito)

