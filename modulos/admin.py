# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Especie
from .models import Categoria
from .models import Usuario
from .models import Comentario_especies

# Register your models here.
admin.site.register(Especie)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Comentario_especies)

