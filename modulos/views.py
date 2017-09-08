# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Especie
from .models import UserForm
from .models import EspecieForm
from .models import Usuario
from .models import Comentario_especies


# Create your views here.


def index(request):
    # obtener lista de especies almacenados en la db
    categoria = request.GET.get('categoria')
    print(categoria)
    if categoria == None or categoria == '':
        lista_especies = Especie.objects.all()
        context = {'lista_especies': lista_especies}
        return render(request, 'modulos/index.html', context)
    else:
        lista_especies = Especie.objects.filter(categoria=categoria)
        context = {'lista_especies': lista_especies}
        return render(request, 'modulos/index.html', context)


def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            firstname = cleaned_data.get('firstname')
            lastname = cleaned_data.get('lastname')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
        user_model = User.objects.create_user(username=username, password=password)
        user_model.firstname = firstname
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('reload'))
        else:
            mensaje = 'Nombre de usuario o clave invalida'

    return render(request, 'modulos/login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def reload(request):
    # obtener lista de especies almacenados en la db
    context = {}
    return render(request, 'modulos/reload.html', context)


def view_detail(request, especie_id):
    especie = Especie.objects.get(id=especie_id)
    context = {'especie': especie}
    return render(request, 'modulos/detail.html', context)


def edit_request(request):
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        User.objects.filter(username=request.user.username).update(first_name=request.POST.get('firstname'))
        User.objects.filter(username=request.user.username).update(last_name=request.POST.get('lastname'))
        User.objects.filter(username=request.user.username).update(email=request.POST.get('email'))

        return HttpResponseRedirect(reverse('reload'))
    else:
        context = {'current_user': current_user}
    return render(request, 'modulos/editar.html', context)


def add_especie(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = EspecieForm()

    return render(request, 'modulos/especie_form.html', {'form': form})


def add_comment(request, especie_id):
    if request.method == 'POST':
        Especie.objects.filter(id=especie_id).update(comentario=request.POST.get('comentario'))
        email = request.POST.get('user')
        comment = request.POST.get('comentario')
        commentObj = Comentario_especies(correo=email, comentario=comment, id_especie=especie_id)
        commentObj.save()

        return HttpResponseRedirect(reverse('reload'))


# REST SERVICES
@csrf_exempt
def get_all_species(request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}
    return HttpResponse(serializers.serialize("json", lista_especies))


@csrf_exempt
def search_specie(response, especie_id):
    lista_especies = Especie.objects.filter(id=especie_id)
    context = {'lista_especies': lista_especies}
    return HttpResponse(serializers.serialize("json", lista_especies))


@csrf_exempt
def search_type(response, categoria):
    lista_especies = Especie.objects.filter(categoria=categoria)
    context = {'lista_especies': lista_especies}
    return HttpResponse(serializers.serialize("json", lista_especies))
