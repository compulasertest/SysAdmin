from django.shortcuts import render

def facturas_list(request):
    return render(request, 'facturacion/facturas_list.html', {})
