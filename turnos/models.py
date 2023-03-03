from django.db import models
# Create your models here.


class Usuarios(models.Model):
    usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=300)
    telefono = models.IntegerField()

