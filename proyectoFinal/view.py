from django.http import HttpResponse
from datetime import datetime
from django.template import loader


def inicio(request):
    return HttpResponse(f'Hola soy Inicio proyectoFinal')

def saludo(request):

    dia = datetime.now()
    return HttpResponse(f'Hola cheeeee, hoy es {dia.strftime("%A %d %B")}')

def templateVista(self):

    nom = "Amaro"
    ap = "El Crack"

    diccionario = {"nombre":nom, "apellido":ap}

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)