from django.urls import path
from AppDonar.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('AppDonar/ropa/', ropa),
    path('AppDonar/utensilio/', utensilio),
    path('AppDonar/mascota/', mascota),
    path('AppDonar/home/', home),
    # APIS
    path('AppDonar/api_ropa/', api_ropa),
    path('AppDonar/api_utensilio/', api_utensilio),
    path('AppDonar/api_mascota/', api_mascota),
    # BUSCAR
    path('AppDonar/buscar_ropa/', buscar_ropa),
    path('AppDonar/buscar_utensilio/', buscar_utensilio),
    path('AppDonar/buscar_mascota/', buscar_mascota),
    # CRUD ROPA
    path('AppDonar/create_ropa/', create_ropa),
    path('AppDonar/read_ropa/', read_ropa),
    path('AppDonar/update_ropa/<ropa_id>', update_ropa),
    path('AppDonar/delete_ropa/<ropa_id>', delete_ropa),
    # CRUD MASCOTA
    path('AppDonar/create_mascota/', create_mascota),
    path('AppDonar/read_mascota/', read_mascota),
    path('AppDonar/update_mascota/<mascota_id>', update_mascota),
    path('AppDonar/delete_mascota/<mascota_id>', delete_mascota),
    # CRUD UTENSILIO
    path('AppDonar/create_utensilio/', create_utensilio),
    path('AppDonar/read_utensilio/', read_utensilio),
    path('AppDonar/update_utensilio/<utensilio_id>', update_utensilio),
    path('AppDonar/delete_utensilio/<utensilio_id>', delete_utensilio),
    # LOGIN
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view(template_name='inicio.html'), name='Logout'),
    # PERFIL
    path('perfil/', perfilView),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass),
    # AVATAR
    path('perfil/changeAvatar/', agregarAvatar),
]
