from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ropa(models.Model):

    tipo = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    email = models.EmailField()
    imagen = models.ImageField(upload_to='articulos', null = True, blank = True)

    def __str__(self):
        return f'Tipo: {self.tipo} | Talle: {self.talle} | Color: {self.color} | Email: {self.email} '

class Utensilio(models.Model):

    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fechaElab = models.DateField()
    email = models.EmailField()
    imagen = models.ImageField(upload_to='articulos', null = True, blank = True)

    def __str__(self):
        return f'Tipo: {self.tipo} | Color: {self.color} | Fecha elaboración: {self.fechaElab} | Email: {self.email} '
        
class Mascota(models.Model):

    tipo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    edad = models.IntegerField()
    castracion = models.BooleanField()
    email = models.EmailField()
    imagen = models.ImageField(upload_to='articulos', null = True, blank = True)

    def __str__(self):
        return f'Tipo: {self.tipo} | Género: {self.genero} | Edad: {self.edad} | Castración: {self.castracion} | Email: {self.email} '

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)