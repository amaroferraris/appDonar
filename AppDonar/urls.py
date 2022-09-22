from django.urls import path
from AppDonar.views import *

urlpatterns = [
    path('', home),
    path('AppDonar/ropa/', ropa),
    path('AppDonar/utensilio/', utensilio),
    path('AppDonar/mascota/', mascota),
    path('AppDonar/home/', home),
]