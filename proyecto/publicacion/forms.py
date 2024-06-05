from django import forms
from .models import Publicacion, Profesor, Materia
from django.utils import timezone

class PublicacionForm(forms.Form):
    profesor = forms.CharField(max_length=100)
    materia = forms.CharField(max_length=100)
    titulo = forms.CharField(max_length=50)
    comentario = forms.CharField(max_length=500, widget=forms.Textarea)
    dominio = forms.IntegerField(min_value=0, max_value=10)
    puntualidad = forms.IntegerField(min_value=0, max_value=10)
    asistencia = forms.IntegerField(min_value=0, max_value=10)
    dificultad = forms.IntegerField(min_value=0, max_value=10)
    seguimiento = forms.IntegerField(min_value=0, max_value=10)

   
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError('Título muy corto.')
        if len(titulo) > 50:
            raise forms.ValidationError('Título muy largo.')
        return titulo
    
    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        if len(comentario) < 10:
            raise forms.ValidationError('Comentario muy corto.')
        if len(comentario) > 500:
            raise forms.ValidationError('Comentario muy largo.')
        return comentario
    
    def clean_profesor(self):
        profesor = self.cleaned_data.get('profesor')
        if not Profesor.objects.filter(nombre=profesor).exists():
            raise forms.ValidationError('Debe seleccionar un profesor.')
        return profesor
    
    def clean_materia(self):
        materia = self.cleaned_data.get('materia')
        if not Materia.objects.filter(nombre=materia).exists():
            raise forms.ValidationError('Debe seleccionar una materia.')
        return materia
    
    def clean(self):
        datos = self.cleaned_data
        profesor = datos.get('profesor')
        materia = datos.get('materia')
        titulo = datos.get('titulo')
        comentario = datos.get('comentario')
        if not all([profesor, materia, titulo, comentario]):
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return datos
    
    def save(self, usuario):
        datos = self.cleaned_data

        profesor = Profesor.objects.get(nombre=datos['profesor'])
        materia = Materia.objects.get(nombre=datos['materia'])

        publicacion = Publicacion(
            usuario=usuario,
            profesor=profesor,
            materia=materia,
            titulo=datos['titulo'],
            comentario=datos['comentario'],
            dominio=datos['dominio'],
            puntualidad=datos['puntualidad'],
            asistencia=datos['asistencia'],
            dificultad=datos['dificultad'],
            seguimiento=datos['seguimiento'],
            fecha=timezone.now()
        )
        publicacion.save()
        return publicacion
    
