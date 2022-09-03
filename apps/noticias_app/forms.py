from cProfile import label
from pyexpat import model
from django import forms
from .models import Comentarios

class FormComment(forms.Form):
	model = Comentarios
	fields = ('cuerpo_comentario')

	cuerpo_comentario = forms.CharField(label='Escribenos tu comentario',widget=forms.Textarea)