from django.shortcuts import render
from django.http import HttpResponse
from AppDonar.models import Mascota, Ropa, Utensilio
from AppDonar.forms import *


def inicio(request):
    return render(request, "inicio.html")

def home(request):
    return render(request, "home.html")

def ropa(request):
        if request.method == 'POST':
            ropa = Ropa(tipo = request.POST['tipo'], talle = request.POST['talle'],
            color = request.POST['color'], email = request.POST['email'])
            ropa.save()
            return render(request, "home.html")
        return render(request, "ropa.html")


def utensilio(request):
    if request.method == 'POST':
        utensilio = Utensilio(tipo = request.POST['tipo'], color = request.POST['color'], fechaElab = request.POST['fechaElab'],
        email = request.POST['email'])
        utensilio.save()
        return render(request, "home.html")
    return render(request, "utensilio.html")

def mascota(request):
    if request.method == 'POST':
        mascota = Mascota(tipo = request.POST['tipo'], genero = request.POST['genero'],
        tamaño = request.POST['tamaño'], edad = request.POST['edad'],
        castracion = request.POST['castracion'], email = request.POST['email'])
        mascota.save()
        return render(request, "home.html")
    return render(request, "mascota.html")

### APIS ###

def api_ropa(request):
    if request.method == "POST":
        formulario = form_ropa(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            ropa = Ropa(tipo = informacion['tipo'], talle = informacion['talle'],
            color = informacion['color'], email = informacion['email'])
            ropa.save()
            return render(request, "api_ropa.html")
    else:
        formulario = form_ropa()
    return render(request, "api_ropa.html", {"formulario":formulario})

def api_utensilio(request):
    if request.method == "POST":
        formulario = form_utensilio(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            utensilio = Utensilio(tipo = informacion['tipo'], color = informacion['color'],
            fechaElab = informacion['fechaElab'], email = informacion['email'])
            utensilio.save()
            return render(request, "api_utensilio.html")
    else:
        formulario = form_utensilio()
    return render(request, "api_utensilio.html", {"formulario":formulario})   

def api_mascota(request):
    if request.method == "POST":
        formulario = form_mascota(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            mascota = Mascota(tipo = informacion['tipo'], genero = informacion['genero'],
            tamaño = informacion['tamaño'], edad = informacion['edad'], castracion = informacion['castracion'],
            email = informacion['email'])
            mascota.save()
            return render(request, "api_mascota.html")
    else:
        formulario = form_mascota()
    return render(request, "api_mascota.html", {"formulario":formulario})

### BUSCAR ###

def buscar_ropa(request):
    if request.GET:
        tipo = request.GET["tipo"]
        ropa = Ropa.objects.filter(tipo__icontains = tipo)
        return render(request, "ropa.html", {"ropa":ropa})
    else:
        respuesta = "No disponible"
    return HttpResponse(respuesta)

def buscar_utensilio(request):
    if request.GET:
        tipo = request.GET["tipo"]
        utensilio = Utensilio.objects.filter(tipo__icontains = tipo)
        return render(request, "utensilio.html", {"utensilio":utensilio})
    else:
        respuesta = "No disponible"
    return HttpResponse(respuesta)

def buscar_mascota(request):
    if request.GET:
        tipo = request.GET["tipo"]
        mascota = Mascota.objects.filter(tipo__icontains = tipo)
        return render(request, "mascota.html", {"mascota":mascota})
    else:
        respuesta = "No disponible"
    return HttpResponse(respuesta)