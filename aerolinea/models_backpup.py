from django.db import models

		

class Pais(models.Model):
	pais = models.CharField(max_length=200)
	
	def __str__(self):
		return self.pais

class Cliente(models.Model):
	TIPO_DOCUMENTO = (
		('DNI', 'DNI'),
		('C','Cedula'),
		('TI','TI'),
		('P','Pasaporte'),
		('CDE','Cedula de extranjeria')
			)
	tipo_documento = models.CharField(max_length=60,choices=TIPO_DOCUMENTO)
	numero_documento = models.PositiveIntegerField(primary_key=True)
	nombre = models.CharField(max_length=200)
	correo = models.EmailField()
	SEXO = (
		('M', 'Masculino'),
		('F','Femenino'))
	sexo = models.CharField(max_length=1,choices=SEXO)
	telefono = models.PositiveIntegerField()
	fecha_nacimiento = models.DateField()
	pais = models.ForeignKey(Pais)
	millas_acum = models.PositiveIntegerField()

	def __str__(self):
		formato = self.nombre + ' Documento: ' + str(self.numero_documento) 
		return formato


class Vuelo(models.Model):
	origen = models.CharField(max_length=200)
	destino = models.CharField(max_length=200)
	TIPO_VUELO = (
		('T','Turista'),
		('E','Ejecutivo')
		)
	tipo_vuelo = models.CharField(max_length=1,choices=TIPO_VUELO)
	fecha_vuelo = models.DateTimeField()
	puesto = models.CharField(max_length=4)
	cliente = models.ForeignKey(Cliente)

	def __str__(self):
		formato = self.id, 
		return formato
