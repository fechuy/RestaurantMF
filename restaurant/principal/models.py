from django.db import models

# Create your models here.

class Reservaciones(models.Model):
	id_reservacion = models.AutoField(primary_key = True)
	fecha_reservacion = models.DateField()
	hora_reservacion = models.TimeField()
	num_personas = models.IntegerField()
	nombre_reservacion = models.CharField(max_length = 100)
	telefono_reservacion = models.BigIntegerField()
	correo_reservacion = models.CharField(max_length = 100)