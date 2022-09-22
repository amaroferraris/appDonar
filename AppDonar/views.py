from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "inicio.html")

def home(request):
    return render(request, "home.html")

def ropa(request):
    return render(request, "ropa.html")

def utensilio(request):
    return render(request, "utensilio.html")

def mascota(request):
    return render(request, "mascota.html")

