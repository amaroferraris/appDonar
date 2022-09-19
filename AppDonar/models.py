from django.db import models

# Create your models here.
class Ropa(models.Model):

    tipo = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    email = models.EmailField()

class Utensilio(models.Model):

    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fechaElab = models.DateField()
    email = models.EmailField()

class Mascota(models.Model):

    tipo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    edad = models.IntegerField()
    castracion = models.BooleanField()
    email = models.EmailField()
