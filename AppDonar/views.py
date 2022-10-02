from django.shortcuts import render, redirect
from django.http import HttpResponse
from traitlets import Instance
from AppDonar.models import Mascota, Ropa, Utensilio
from AppDonar.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

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
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # print(form) para debuggear
        if form.is_valid():

            form.save()
            return redirect("/login/")

    else:

        return render(request, "registro.html", {"form":form})

    form = UserRegisterForm()
    return render(request, "registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    form = UserEditForm(request.POST, instance = usuario)
    if request.method == 'POST':
        if form.is_valid():
            # Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.fist_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'home.html')
        else:
            return render(request, 'home.html', {"form":form})
    else:
        form = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username,
                            'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, 'editarPerfil.html', {'form':form, 'usuario':usuario})

@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        # form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'home.html')
    else:
        # form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form':form, 'usuario':usuario})

@login_required
def perfilView(request):
    return render(request, 'perfil.html')