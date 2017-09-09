# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm


class Especie(models.Model):
    nombre = models.CharField(max_length=100)
    clasificacionTax = models.CharField(max_length=500)
    nombreCientifico = models.CharField(max_length=300)
    categoria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    imageFile = models.ImageField(upload_to='static/img', null=True)
    comentario = models.CharField(max_length=100)
class Categoria(models.Model):
    url = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=100)
    nombreEspecie = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Comentario_especies(models.Model):
    id_especie = models.CharField(max_length=50, unique=True, null=True)
    correo = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    intereses = models.CharField(max_length=1000)


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput())
    password2 = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password', 'password2']


class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields= ['nombre','clasificacionTax','nombreCientifico','categoria','descripcion','url','imageFile']

def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username):
        raise forms.ValidationError('Nombre de usuario ya existe')
    return username


def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email):
        raise forms.ValidationError('El correo ya fue usado')
    return email


def clean_username(self):
    password= self.cleaned_data['password']
    password2 = self.cleaned_data['password2']
    if password != password2:
        raise forms.ValidationError('Las contraseñas no coincidenNombre de usuario ya existe')
    return password


class correoform(forms.ModelForm):
    correo = forms.EmailField()
    mensaje = forms.Textarea()

    class Meta:
        model = Comentario_especies
        fields = ['correo', 'comentario']