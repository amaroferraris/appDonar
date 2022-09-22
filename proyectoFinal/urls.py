from django.contrib import admin
from django.urls import path, include
from proyectoFinal.view import *
from proyectoFinal.view import inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('saludo/', saludo),
    path('template/', templateVista),
    path('AppDonar/', include("AppDonar.urls")),
]
