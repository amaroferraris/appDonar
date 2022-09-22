from django.urls import path
from AppDonar.views import *

urlpatterns = [
    path('', inicio),
    path('ropa/', ropa),
    path('utensilio/', utensilio),
    path('mascota/', mascota),
    path('home/', home),
]