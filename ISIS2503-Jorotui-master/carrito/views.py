from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Carrito
from .forms import CarritoForm
from ..variables.forms import VariableForm
from ..variables.models import Variable

# Create your views here.
@login_required
def modificar_carrito(request, carrito_id):
    instancia = Carrito.objects.get(id=carrito_id)
    form = CarritoForm(instance=instancia)
    if request.method == 'POST':
        form = CarritoForm(request.POST, instance=instancia)
        if form.is_valid():

            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "Carrito/carritoEdit.html", {'form': form})

@login_required
def añadir_carrito(request, carrito_id, variable_id):
    instanciaVariable = Variable.object.get(id=variable_id)
    instancia = Carrito.objects.get(id=carrito_id)
    instancia.productos[len(instancia.productos)] = instanciaVariable
    instancia.cantidadProductos = instancia.cantidadProductos + 1
    instancia.costoTotal = instancia.costoTotal + instanciaVariable.costo
    if instanciaVariable.cantidad>0:
        instanciaVariable.cantidad = instanciaVariable.cantidad-1
    form = CarritoForm(instance=instancia)
    formVariable = VariableForm(instance=instanciaVariable)
    if request.method == 'POST':
        form = CarritoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            instanciaVariable = formVariable.save(commit=False)
            instanciaVariable.save()
    return render(request, "Carrito/addToCart.html", {'form': form})
