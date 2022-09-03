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
from .forms import FormComment

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
        "noticias": lista_noticias,
    }
    return render(request,'noticias.html', context)



def detallenoticia(request, id):
    try:
        noticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = Comentarios(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("detalle-noticia", id=noticia.id)

    context = {
        "form":form,
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'detalle-noticia.html', context)


def conocenos(request):
    return render(request,'conocenos.html', {})

def eventos(request):
    return render(request,'eventos.html', {})


@login_required
def commentAproved(request, id):
    try:
        comentario = Comentarios.objects.get(id=id)
    except Comentarios.DoesNotExist:
        raise Http404("Inexistente")

    comentario.approve()
    return redirect("detalle-noticia", id=comentario.noticia.id)