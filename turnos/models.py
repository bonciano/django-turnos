from django.db import models
# Create your models here.


class Usuarios(models.Model):
    usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=300)
    telefono = models.IntegerField()


class Turnos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    disponible = models.BooleanField(default=False)

class Mensajes(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=300)
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=300)
