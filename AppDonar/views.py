from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppDonar.models import Mascota, Ropa, Utensilio
from AppDonar.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio.html")

@login_required

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

### CRUD ###

def create_ropa(request):
    if request.method == "POST":
        ropa = Ropa(tipo = request.POST['tipo'], talle = request.POST['talle'], 
        color = request.POST['color'], email = request.POST['email'])
        ropa.save()
        ropa = Ropa.objects.all()
        return render(request, "ropaCRUD/read_ropa.html", {"ropa":ropa})
    return render(request, "ropaCRUD/create_ropa.html")

def read_ropa(request):
    ropa = Ropa.objects.all()
    return render(request, "ropaCRUD/read_ropa.html", {"ropa":ropa})

def update_ropa(request, ropa_id):
    ropa = Ropa.objects.get(id = ropa_id)

    if request.method == 'POST':
        formulario = form_ropa(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            ropa.tipo = informacion['tipo']
            ropa.talle = informacion['talle']
            ropa.color = informacion['color']
            ropa.email = informacion['email']
            ropa.save()
            ropa = Ropa.objects.all()
        return render(request, "ropaCRUD/read_ropa.html", {"ropa":ropa})
    else:
        formulario = form_ropa(initial={"tipo" : ropa.tipo, "talle" : ropa.talle, "color" : ropa.color, "email" : ropa.email})
    return render(request, "ropaCRUD/update_ropa.html", {"formulario":formulario})

def delete_ropa(request, ropa_id):
    ropa = Ropa.objects.get(id = ropa_id)
    ropa.delete()
    ropa = Ropa.objects.all()
    return render(request, "ropaCRUD/read_ropa.html", {"ropa":ropa})
######################################################################
def create_mascota(request):
    if request.method == "POST":
        mascota = Mascota(tipo = request.POST['tipo'], genero = request.POST['genero'], 
        tamaño = request.POST['tamaño'], edad = request.POST['edad'], castracion = request.POST['castracion'],
        email = request.POST['email'])
        mascota.save()
        mascota = Mascota.objects.all()
        return render(request, "mascotaCRUD/read_mascota.html", {"mascota":mascota})
    return render(request, "mascotaCRUD/create_mascota.html")

def read_mascota(request):
    mascota = Mascota.objects.all()
    return render(request, "mascotaCRUD/read_mascota.html", {"mascota":mascota})

def update_mascota(request, mascota_id):
    mascota = Mascota.objects.get(id = mascota_id)

    if request.method == 'POST':
        formulario = form_mascota(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            mascota.tipo = informacion['tipo']
            mascota.genero = informacion['genero']
            mascota.tamaño = informacion['tamaño']
            mascota.edad = informacion['edad']
            mascota.castracion = informacion['castracion']
            mascota.email = informacion['email']
            mascota.save()
            mascota = Mascota.objects.all()
        return render(request, "mascotaCRUD/read_mascota.html", {"mascota":mascota})
    else:
        formulario = form_mascota(initial={"tipo" : mascota.tipo, "genero" : mascota.genero, "tamaño" : mascota.tamaño, 
        "edad" : mascota.edad, "castracion" : mascota.castracion, "email" : mascota.email})
    return render(request, "mascotaCRUD/update_mascota.html", {"formulario":formulario})

def delete_mascota(request, mascota_id):
    mascota = Mascota.objects.get(id = mascota_id)
    mascota.delete()
    mascota = Mascota.objects.all()
    return render(request, "mascotaCRUD/read_mascota.html", {"mascota":mascota})
######################################################################
def create_utensilio(request):
    if request.method == "POST":
        utensilio = Utensilio(tipo = request.POST['tipo'], color = request.POST['color'], 
        fechaElab = request.POST['fechaElab'], email = request.POST['email'])
        utensilio.save()
        utensilio = Utensilio.objects.all()
        return render(request, "utensilioCRUD/read_utensilio.html", {"utensilio":utensilio})
    return render(request, "utensilioCRUD/create_utensilio.html")

def read_utensilio(request):
    utensilio = Utensilio.objects.all()
    return render(request, "utensilioCRUD/read_utensilio.html", {"utensilio":utensilio})

def update_utensilio(request, utensilio_id):
    utensilio = Utensilio.objects.get(id = utensilio_id)

    if request.method == 'POST':
        formulario = form_utensilio(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            utensilio.tipo = informacion['tipo']
            utensilio.color = informacion['color']
            utensilio.fechaElab = informacion['fechaElab']
            utensilio.email = informacion['email']
            utensilio.save()
            utensilio = Utensilio.objects.all()
        return render(request, "utensilioCRUD/read_utensilio.html", {"utensilio":utensilio})
    else:
        formulario = form_utensilio(initial={"tipo" : utensilio.tipo, "color" : utensilio.color, 
        "fechaElab" : utensilio.fechaElab, "email" : utensilio.email})
    return render(request, "utensilioCRUD/update_utensilio.html", {"formulario":formulario})

def delete_utensilio(request, utensilio_id):
    utensilio = Utensilio.objects.get(id = utensilio_id)
    utensilio.delete()
    utensilio = Utensilio.objects.all()
    return render(request, "utensilioCRUD/read_utensilio.html", {"utensilio":utensilio})


##########  L O G I N  #################
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {"form":form})
        else:
            return render(request, "login.html", {"form":form})
    form = AuthenticationForm()
    return render(request, 'login.html', {"form":form})

def registro(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data["username"]
            form.save()
            return redirect("/login/")
    # form = UserCreationForm()
    else:
        form = UserRegisterForm()
        return render(request, "registro.html", {"form":form})