import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Regimen(models.Model):
	regimen        = models.CharField(max_length=80)

	def __str__(self):
		return self.regimen

class Cp(models.Model):
	cp             = models.IntegerField()
	colonia        = models.CharField(max_length=80)
	localidad      = models.CharField(max_length=80, default='Nogales')
	municipio      = models.CharField(max_length=80, default='Nogales')
	estado         = models.CharField(max_length=80, default='Sonora')
	pais           = models.CharField(max_length=50, default='Mexico')

	def __str__(self):
		return '%s %s %s %s %s %s' % (self.cp, self.colonia, self.localidad, self.municipio, self.estado, self.pais)

class Empresa(models.Model):
	user           = models.OneToOneField(User)
	rfc            = models.CharField(max_length=13)
	nombre         = models.CharField(max_length=80)
	direccion      = models.CharField(max_length=80)
	no_int         = models.CharField(max_length=30)
	no_ext         = models.CharField(max_length=30, blank=True)
	cp             = models.ForeignKey(Cp)
	colonia        = models.CharField(max_length=80)
	telefono1      = models.CharField(max_length=10, blank=True)
	telefono2      = models.CharField(max_length=10, blank=True)
	email1         = models.EmailField('e-mail', blank=True)
	email2         = models.EmailField('e-mail', blank=True)
	cer            = models.CharField(max_length=100, blank=True)
	key            = models.CharField(max_length=100, blank=True)
	pwd            = models.CharField(max_length=32, blank=True)
	regimen        = models.ForeignKey(Regimen) 
	serie_f        = models.CharField(max_length=10, blank=True)
	created_date   = models.DateTimeField( default=timezone.now)
	published_date = models.DateTimeField( blank=True, null=True)

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s' % (self.rfc, self.nombre, self.direccion, self.no_int, self.no_ext, self.cp, self.colonia, self.regimen, self.telefono1, self.telefono2, self.email1, self.email2)

class Cliente(models.Model):
	rfc            = models.CharField(max_length=13, unique=True)
	nombre         = models.CharField(max_length=100)

	def __str__(self):
		return '%s %s'%(self.rfc, self.nombre)

class Sucursal(models.Model):
	rfc            = models.ForeignKey(Cliente)
	direccion      = models.CharField(max_length=80)
	no_int         = models.CharField(max_length=30)
	no_ext         = models.CharField(max_length=30, blank=True)
	cp             = models.ForeignKey(Cp)
	colonia        = models.CharField(max_length=80)
	telefono1      = models.CharField(max_length=10, blank=True)
	telefono2      = models.CharField(max_length=10, blank=True)
	email1         = models.EmailField('e-mail', blank=True)
	email2         = models.EmailField('e-mail', blank=True)
	email3         = models.EmailField('e-mail', blank=True)
	no_cuenta      = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return '%s %s %s %s %s %s %s %s'%(self.rfc, self.direccion, self.no_int, self.no_ext, self.cp, self.colonia, self.telefono1, self.email1)

class Factura(models.Model):
	MONEDA = (
		('P', 'Pesos'),
		('D', 'Dolares Americanos')
	)
	serie          = models.CharField(max_length=10)                 
	factura        = models.IntegerField()
	cliente        = models.ForeignKey(Cliente)
	no_orden       = models.CharField(max_length=20, blank=True)
	fecha          = models.DateField(blank=True, null=True)
	tipo_cambio    = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
	moneda         = models.CharField(max_length=1, choices=MONEDA)
	importe        = models.DecimalField(max_digits=13,decimal_places=2,blank=True, null=True)
	descuento      = models.DecimalField(max_digits=13,decimal_places=2,blank=True, null=True)
	iva            = models.DecimalField(max_digits=12,decimal_places=2,blank=True, null=True)
	riva           = models.DecimalField(max_digits=12,decimal_places=2,blank=True, null=True)
	risr           = models.DecimalField(max_digits=13,decimal_places=2,blank=True, null=True)
	tiva           = models.DecimalField(max_digits=4,decimal_places=2,blank=True, null=True)
	triva          = models.DecimalField(max_digits=4,decimal_places=2,blank=True, null=True)
	trisr          = models.DecimalField(max_digits=4,decimal_places=2,blank=True, null=True)
	fecha_emision  = models.DateTimeField( default=timezone.now)
	forma_pago     = models.CharField(max_length=80)
	metodo_pago    = models.CharField(max_length=80)
	cond_pago      = models.CharField(max_length=80)
	num_cta_pago   = models.CharField(max_length=10,blank=True)
	inf_aduanera   = models.BooleanField()
	num_pedimento  = models.CharField(max_length=30,blank=True)
	aduana         = models.CharField(max_length=30,blank=True)
	fecha_pedimento= models.DateField(blank=True, null=True)
	motivo_descto  = models.CharField(max_length=60,blank=True)
	uuid           = models.UUIDField(editable=False, default=uuid.uuid4)

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s' % (self.serie, self.factura, self.cliente, self.no_orden, self.fecha, self.importe, self.descuento, self.iva, self.riva, self.risr, self.fecha_emision, self.uuid)