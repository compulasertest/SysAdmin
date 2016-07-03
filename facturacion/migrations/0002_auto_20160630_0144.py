# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=80)),
                ('no_int', models.CharField(max_length=30)),
                ('no_ext', models.CharField(max_length=30)),
                ('colonia', models.CharField(max_length=80)),
                ('telefono1', models.CharField(max_length=10)),
                ('telefono2', models.CharField(max_length=10)),
                ('email1', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('email2', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('cer', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('cp', models.ForeignKey(to='facturacion.Cp')),
                ('regimen', models.ForeignKey(to='facturacion.Regimen')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='cp',
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='regimen',
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='user',
        ),
        migrations.DeleteModel(
            name='Empresas',
        ),
    ]
