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
    imagen = forms.ImageField()

class form_utensilio(forms.Form):

    tipo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Cama/Heladera/Etc'}))
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Blanco/Verde/Etc'}))
    fechaElab = forms.DateField(label='Fecha de elaboración', widget=forms.TextInput(attrs={'placeholder': 'AAAA-MM-DD'}))
    email = forms.EmailField(label='Contacto', widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    imagen = forms.ImageField()

class form_mascota(forms.Form):
    tipo = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'perro / gato / etc'}))
    genero = forms.CharField(max_length=50, label='Género', widget=forms.TextInput(attrs={'placeholder': 'macho / hembra'}))
    tamaño = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'chico / mediano / grande'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'años'}))
    castracion = forms.BooleanField(required=False, label='Castrado/a')
    email = forms.EmailField(label='Contacto', widget=forms.TextInput(attrs={'placeholder': 'tuemail@gmail.com'}))
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Last name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Confirm new password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}

class avatarFormulario(forms.Form):
   avatar = forms.ImageField()

