from django.db import models

# Create your models here.
class Ropa(models.Model):

    tipo = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'Tipo: {self.tipo} | Talle: {self.talle} | Color: {self.color} | Email: {self.email} '

class Utensilio(models.Model):

    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fechaElab = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'Tipo: {self.tipo} | Color: {self.color} | Fecha elaboración: {self.fechaElab} | Email: {self.email} '
        
class Mascota(models.Model):

    tipo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    edad = models.IntegerField()
    castracion = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return f'Tipo: {self.tipo} | Género: {self.genero} | Edad: {self.edad} | Castración: {self.castracion} | Email: {self.email} '