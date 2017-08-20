# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Especie(models.Model):
    nombre = models.CharField(max_length=100)
    clasificacionTax = models.CharField(max_length=100)
    nombreCientifico = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)


class Categoria(models.Model):
    url = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=100)
    nombreEspecie = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)


class Comentario(models.Model):
    correo = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    intereses = models.CharField(max_length=1000)

