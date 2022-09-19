from django.contrib import admin
from django.urls import path
from proyectoFinal.view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('template/', templateVista),
]
