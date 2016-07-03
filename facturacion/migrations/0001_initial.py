# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cp', models.IntegerField()),
                ('colonia', models.CharField(max_length=80)),
                ('localidad', models.CharField(default=b'Nogales', max_length=80)),
                ('municipio', models.CharField(default=b'Nogales', max_length=80)),
                ('estado', models.CharField(default=b'Sonora', max_length=80)),
                ('pais', models.CharField(default=b'Mexico', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
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
            ],
        ),
        migrations.CreateModel(
            name='Regimen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regimen', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='empresas',
            name='regimen',
            field=models.ForeignKey(to='facturacion.Regimen'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
