from django.db import models

		
class Cliente(models.Model):
	id_cliente = models.PositiveIntegerField(primary_key=True)
	nombre = models.CharField(max_length=200)
	edad = models.PositiveIntegerField(max_length=2)
	telefono = models.PositiveIntegerField()
	correo = models.EmailField()
	SEXO = (
		('M', 'Masculino'),
		('F','Femenino'))
	sexo = models.CharField(max_length=1,choices=SEXO)

	def __str__(self):
		return self.nombre



class Compania(models.Model):
	id_compania = models.PositiveIntegerField()
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.PositiveIntegerField()

	def __str__(self):
		return self.nombre


class Origen(models.Model):
	nAeropuerto = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)

	def __str__(self):
		return self.ciudad

class Destino(models.Model):
	nAeropuerto = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)

	def __str__(self):
		return self.ciudad
		

class Itinerario(models.Model):
	id_itinerario = models.PositiveIntegerField(primary_key=True)
	hora = models.DateTimeField()
	fecha = models.DateField()
	origen = models.ForeignKey(Origen)
	destino = models.ForeignKey(Destino)

	def __str__(self):
		return str(self.id_itinerario)
	
class Vuelo(models.Model):
	id_vuelo = models.PositiveIntegerField(primary_key=True)
	capacidad = models.PositiveIntegerField()
	modelo_avion = models.CharField(max_length=50)
	numero_vuelo = models.CharField(max_length=50)
	compania = models.ForeignKey(Compania)
	itinerario = models.ForeignKey(Itinerario)

	def __str__(self):
		return str(self.id_vuelo)



class Pasaje(models.Model):
	numero_pasaje = models.PositiveIntegerField(primary_key=True)
	TIPO_VUELO = (
		('T','Turista'),
		('E','Ejecutivo'),
		)
	clase = models.CharField(max_length=1,choices=TIPO_VUELO)
	asiento = models.CharField(max_length=50)
	valor = models.PositiveIntegerField()
	cliente = models.ForeignKey(Cliente)
	vuelo = models.ForeignKey(Vuelo)
	
	def __str__(self):
		respuesta = str(self.numero_pasaje) + ' clase: ' + self.clase
		return respuesta