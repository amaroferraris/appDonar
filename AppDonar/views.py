from django.shortcuts import render
from django.http import HttResponse

def inicio(request):
    return render(request, "inicio.html")

def ropa(request):
    return render(request, "ropas.html")

def utensilio(request):
    return render(request, "utensilios.html")

def mascota(request):
    return render(request, "mascotas.html")
