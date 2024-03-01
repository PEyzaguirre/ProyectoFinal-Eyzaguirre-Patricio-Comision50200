from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Locales(models.Model):
    nombre = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.nombre}"
    

class Productos(models.Model):
    nombre = models.CharField(max_length = 50)
    unidadMedida = models.CharField(max_length = 50)
    tipoProducto = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.nombre}, {self.unidadMedida}"


class Entregas(models.Model):
    fechaEntrega = models.DateField(default=datetime.now, blank=True)
    producto = models.CharField(max_length = 50, default='')
    cantidad = models.IntegerField()
    localDestino = models.CharField(max_length = 50, default='')
    reponedor = models.CharField(max_length = 50, default='')
    fechaVcto = models.DateField(default=datetime.now, blank=True)


class Repartidor(models.Model):
    nombre = models.CharField(max_length = 50)
    rut = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"{self.nombre}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   

 