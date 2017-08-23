# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Especie
# Create your views here.
def index(request):
    # obtener lista de especies almacenados en la db
    lista_especies= Especie.objects.all()
    context ={'lista_especies': lista_especies}
    return render(request,'modulos/index.html',context)
