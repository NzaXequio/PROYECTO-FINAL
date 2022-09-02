from time import timezone
from django.shortcuts import render, redirect
from .models import Noticia,Categoria,Comentarios
from django.http.response import Http404
from django.conf import settings
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .forms import NoticiaForm, CommentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)

# Create your views here.
def index(request):
    #texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    #ultimasnoticias = Noticia.objects.all().order_by('creado').reverse()[:3]
    #context = {
    #    'noticiasdestacadas':ultimasnoticias
    #}
    return render(request, 'index.html',)

def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticia": lista_noticias,
        # "MEDIA_ROOT": 'media/img/noticias/'
        #"MEDIA_ROOT": 'media/img/noticias/'
        #\media\img\noticias\
    }
    return render(request, 'noticias.html',context)

def detallenoticia(request,id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')
    context = {
        "noticias": datanoticia,
        "comentarios":lista_comentarios,
        "MEDIA_ROOT": 'media/img/noticias/'
        
    }
    return render(request,'detalle-noticia.html',context)


def conocenos(request):
    return render(request,'conocenos.html', {})

def eventos(request):
    return render(request,'eventos.html', {})