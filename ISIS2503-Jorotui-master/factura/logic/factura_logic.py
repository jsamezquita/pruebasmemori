from ..models import Factura


def get_factura():
    queryset = Factura.objects.all()
    return (queryset)


def create_factura(form):
    factura = form.save()
    factura.save()
    return ()