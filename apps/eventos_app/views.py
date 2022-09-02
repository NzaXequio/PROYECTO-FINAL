from time import timezone
from django.shortcuts import render, redirect
from .models import Evento,Categoria
from django.http.response import Http404
from django.conf import settings
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .forms import NoticiaForm, CommentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    return render(request, 'noticias.html',{})


def conocenos(request):
    return render(request,'conocenos.html', {})

def eventos(request):
    lista_eventos = Evento.objects.all().order_by('creado')
    context = {
        "evento": lista_eventos,
    }
    return render(request,'eventos.html', {})