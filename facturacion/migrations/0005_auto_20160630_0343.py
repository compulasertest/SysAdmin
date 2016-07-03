# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_auto_20160630_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='uuid',
            field=models.UUIDField(null=True, editable=False, blank=True),
        ),
    ]
