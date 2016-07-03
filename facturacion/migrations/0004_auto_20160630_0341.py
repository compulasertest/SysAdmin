# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20160630_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='motivo_descto',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='uuid',
            field=models.UUIDField(editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='no_cuenta',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
