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

    # BUSCAR
    path('AppDonar/buscar_ropa/', buscar_ropa),
    path('AppDonar/buscar_utensilio/', buscar_utensilio),
    path('AppDonar/buscar_mascota/', buscar_mascota),
    # CRUD (pero sin Create & Read)
    path('AppDonar/update_ropa/<ropa_id>', update_ropa),
    path('AppDonar/delete_ropa/<ropa_id>', delete_ropa),

    path('AppDonar/update_mascota/<mascota_id>', update_mascota),
    path('AppDonar/delete_mascota/<mascota_id>', delete_mascota),

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
