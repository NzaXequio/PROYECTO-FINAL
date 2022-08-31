from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

#def registro(request):
    #return render(request, 'registro.html', {})

def noticias(request):
    return render(request,'noticias.html', {})

def conocenos(request):
    return render(request,'conocenos.html', {})
    
def eventos(request):
    return render(request,'eventos.html', {})