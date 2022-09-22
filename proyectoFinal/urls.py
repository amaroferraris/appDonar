from django.contrib import admin
from django.urls import path, include
from proyectoFinal.view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("AppDonar.urls")),
]
