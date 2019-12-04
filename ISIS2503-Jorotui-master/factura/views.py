from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Factura
from .forms import FacturaForm
from ..variables.forms import VariableForm
from ..variables.models import Variable
from .logic.factura_logic import get_factura, create_factura

# Create your views here.
@login_required
def generar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            create_factura(form)
            messages.add_message(request, messages.SUCCESS, 'Se generó de forma exitosa la factura')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()
    context = {'form': form,}
    return render(request, 'Factura/variableCreate.html', context)
