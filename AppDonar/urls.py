from django.urls import path
from AppDonar.views import *

urlpatterns = [
    path('', home),
    path('AppDonar/ropa/', ropa),
    path('AppDonar/utensilio/', utensilio),
    path('AppDonar/mascota/', mascota),
    path('AppDonar/home/', home),
    path('AppDonar/api_ropa/', api_ropa),
    path('AppDonar/api_utensilio/', api_utensilio),
    path('AppDonar/api_mascota/', api_mascota),
    path('AppDonar/buscar_ropa/', buscar_ropa),
    path('AppDonar/buscar_utensilio/', buscar_utensilio),
    path('AppDonar/buscar_mascota/', buscar_mascota),
]