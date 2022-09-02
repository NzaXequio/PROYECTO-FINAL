from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, help_text='Seleccione una imagen para mostrar') #carpeta img/noticias  uploade_to = 'img/noticias',
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='noticia')

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()

    #def comentariosAprobados(self):
    #    return self.comentarios.filter(aprobado=True)  

# cuando se crea una nueva tabla acá, ejecutar py manage.py makemigrations noticias_app 
# luego py manage.py migrate

class Comentarios(models.Model):
    noticia = models.ForeignKey('Noticia', related_name = 'comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)
    
    def aprobarComentario(self):
        self.aprobado = True
        self.save() 
