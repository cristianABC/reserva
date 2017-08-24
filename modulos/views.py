# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Especie
from .models import UserForm
# Create your views here.


def index(request):
    # obtener lista de especies almacenados en la db
    lista_especies= Especie.objects.all()
    context ={'lista_especies': lista_especies}
    return render(request, 'modulos/index.html', context)


def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            firstname = cleaned_data.get('firstname')
            lastname= cleaned_data.get('lastname')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
        user_model = User.objects.create_user(username=username, password=password)
        user_model.firstname= firstname
        user_model.lastname = lastname
        user_model.email = email
        user_model.save()

        return HttpResponseRedirect(reverse('reload'))
    else:
        form = UserForm()
        context = {'form': form}
    return render(request, 'modulos/registro.html', context)


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    mensaje = ''
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('reload'))
        else:
            mensaje='Nombre de usuario o clave invalida'

    return render(request, 'modulos/login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def reload(request):
    # obtener lista de especies almacenados en la db
    context ={}
    return render(request, 'modulos/reload.html', context)

