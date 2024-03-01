from django import forms
from .models import Productos, Locales, Repartidor, Entregas
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import datetime

class LocalesForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True)
    ubicacion = forms.CharField(max_length = 50, required=True)


class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True)
    unidadMedida = forms.CharField(max_length = 50, required=True, label="Unidad de Medida")   
    tipoProducto = forms.CharField(max_length = 50, required=True, label= "Tipo de Producto")  


class RepartidorForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True, label="Nombre")
    rut = forms.CharField(max_length = 50, required=True, label="RUT")   
    direccion = forms.CharField(max_length = 50, required=True, label= "Dirección")      


class EntregasForm(forms.Form):
    fechaEntrega = forms.DateField(initial=datetime.date.today, label="Fecha Entrega")
    producto = forms.ModelChoiceField(queryset=Productos.objects.all(), empty_label="Seleccione Producto", label="Producto")
    cantidad = forms.IntegerField(label="Cantidad")
    localDestino = forms.ModelChoiceField(queryset=Locales.objects.all(), empty_label="Seleccione Local", label="Local Destino")
    reponedor = forms.ModelChoiceField(queryset=Repartidor.objects.all(), empty_label="Seleccione Reponedor", label="Reponedor")
    fechaVcto = forms.DateField(initial=datetime.date.today, label="Fecha Vcto.")


class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']         


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)        