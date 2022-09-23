from django import forms

class form_ropa(forms.Form):
    tipo = forms.CharField(max_length=50)
    talle = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    email = forms.EmailField()

class form_utensilio(forms.Form):

    tipo = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    fechaElab = forms.DateField()
    email = forms.EmailField()

class form_mascota(forms.Form):
    tipo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    tamaño = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    castracion = forms.BooleanField()
    email = forms.EmailField()