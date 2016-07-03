# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20160630_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rfc', models.CharField(unique=True, max_length=13)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=10)),
                ('factura', models.IntegerField()),
                ('no_orden', models.CharField(max_length=20, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('tipo_cambio', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('moneda', models.CharField(max_length=1, choices=[(b'P', b'Pesos'), (b'D', b'Dolares Americanos')])),
                ('importe', models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)),
                ('descuento', models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)),
                ('iva', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('riva', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('risr', models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)),
                ('tiva', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('triva', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('trisr', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('fecha_emision', models.DateTimeField(default=django.utils.timezone.now)),
                ('forma_pago', models.CharField(max_length=80)),
                ('metodo_pago', models.CharField(max_length=80)),
                ('cond_pago', models.CharField(max_length=80)),
                ('num_cta_pago', models.CharField(max_length=10, blank=True)),
                ('inf_aduanera', models.BooleanField()),
                ('num_pedimento', models.CharField(max_length=30, blank=True)),
                ('aduana', models.CharField(max_length=30, blank=True)),
                ('fecha_pedimento', models.DateField(null=True, blank=True)),
                ('motivo_descto', models.CharField(max_length=60)),
                ('uuid', models.UUIDField(editable=False)),
                ('cliente', models.ForeignKey(to='facturacion.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=80)),
                ('no_int', models.CharField(max_length=30)),
                ('no_ext', models.CharField(max_length=30, blank=True)),
                ('colonia', models.CharField(max_length=80)),
                ('telefono1', models.CharField(max_length=10, blank=True)),
                ('telefono2', models.CharField(max_length=10, blank=True)),
                ('email1', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('email2', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('email3', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('no_cuenta', models.CharField(max_length=10)),
                ('cp', models.ForeignKey(to='facturacion.Cp')),
                ('rfc', models.ForeignKey(to='facturacion.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='serie_f',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cer',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='key',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='no_ext',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='pwd',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono1',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono2',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
