from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Evento
from apps.eventos_app import models
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = ('titulo', 'autor', 'img')

admin.site.register(Evento,EventoAdmin)

#class CategoriasInline(admin.StackedInline):
   # model= Evento.Cateogria.through
   # extra= 5
#admin.site.register(Categoria,admin.ModelAdmin)

