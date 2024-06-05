from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views
from .models import Materia
from publicacion.models import Publicacion

# Create your views here.
class MateriaView(generic.ListView):
    template_name = 'materia/materia.html'
    context_object_name = 'materias'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Materia.objects.filter(nombre__icontains=query).order_by('nombre')
        return Materia.objects.all().order_by('nombre')

class DetalleMateriaView(generic.DetailView):
    model = Materia
    template_name = 'materia/detalleMateria.html'
    context_object_name = 'materia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Rescatar reseñas del profesor
        context['publicaciones'] = Publicacion.objects.filter(materia=self.get_object())

        numPublicaciones = len(context['publicaciones'])
        context['numPublicaciones'] = numPublicaciones

        # Calificación general
        for publicacion in context['publicaciones']:
            # Invertir la dificultad antes de sumarla al cálculo general
            dificultadInvertida = 10 - publicacion.dificultad
            calGeneralPublicacion = (
                publicacion.dominio + 
                publicacion.puntualidad + 
                publicacion.asistencia + 
                dificultadInvertida +  
                publicacion.seguimiento
            ) / 5
            publicacion.calGeneralPublicacion = round(calGeneralPublicacion, 1)
                  
        return context

