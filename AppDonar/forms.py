# from dataclasses import field
# from turtle import write_docstringdict
from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_ropa(forms.Form):
    tipo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'remera / pantalón / zapatillas'}))
    talle = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 's / m / 35 / 42'}))
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'verde / blanco / etc'}))
    email = forms.EmailField(label='Contacto', widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    # imagen = forms.ImageField()

class form_utensilio(forms.Form):

    tipo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'cama / heladera / etc'}))
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'blanco / verde / etc'}))
    fechaElab = forms.DateField(label='Fecha de elaboración', widget=forms.TextInput(attrs={'placeholder': 'AAAA-MM-DD'}))
    email = forms.EmailField(label='Contacto', widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    # imagen = forms.ImageField()

class form_mascota(forms.Form):
    tipo = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'perro / gato / etc'}))
    genero = forms.CharField(max_length=50, label='Género', widget=forms.TextInput(attrs={'placeholder': 'macho / hembra'}))
    tamaño = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'chico / mediano / grande'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'años'}))
    castracion = forms.BooleanField(required=False, label='Castrado/a')
    email = forms.EmailField(label='Contacto', widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    # imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': '*********'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'placeholder': '*********'}))
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Usuario'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Last name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Contraseña actual'}))
    new_password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Contraseña nueva'}))
    new_password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Confirmar contraseña nueva'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}

class avatarFormulario(forms.Form):
   avatar = forms.ImageField()