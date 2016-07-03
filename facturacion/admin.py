from django.contrib import admin
from .models import Regimen, Cp, Empresa, Cliente, Sucursal, Factura

admin.site.register(Regimen)
admin.site.register(Cp)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Factura)