from django.db import models
from ..carrito.models import Carrito
from ..usuarios.models import Usuario

class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete=models.CASCADE, default=None)
    carrito = models.ForeignKey(Carrito, null = False, blank = False, on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)

def __str__(self):
    detallesFactura = []
    i = 0
    while i<len(self.productos):
        detallesFactura[i] = "Nombre producto: "+self.productos[i].name +" Cantidad: "+self.productos[i].cantidad
        i = i+1
    detallesFactura[i] = "Total: " + self.carrito.costoTotal
    detallesFactura[i+1] = "Cliente comprador: "+self.usuario.name
    detallesFactura[i+2] = "Fecha de compra: "+self.fecha

    return '{}'.format(detallesFactura)