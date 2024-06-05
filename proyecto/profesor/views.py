from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.views.generic import TemplateView


from .models import Profesor
from publicacion.models import Publicacion

# Create your views here.
class ProfesorView(generic.ListView):
    template_name = 'profesor/profesor.html'
    context_object_name = 'profesores'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Profesor.objects.filter(nombre__icontains=query).order_by('nombre')
        return Profesor.objects.all().order_by('nombre')


class PerfilProfesorView(generic.DetailView):
    model = Profesor
    template_name = 'profesor/perfilProfesor.html'
    context_object_name = 'profesor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Rescatar reseñas del profesor
        context['publicaciones'] = Publicacion.objects.filter(profesor=self.get_object())

        numPublicaciones = len(context['publicaciones'])
        context['numPublicaciones'] = numPublicaciones

        # Calificaciones generales
        calidadGeneral = 0
        dificultadGeneral = 0
        dominioGeneral = 0
        puntualidadGeneral = 0
        asistenciaGeneral = 0
        seguimientoGeneral = 0

        if numPublicaciones == 0:
            return context

        # Calcular calificacion general de cada publicación
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
            
            # Calcular calificaciones generales acumuladas
            calidadGeneral += calGeneralPublicacion
            dificultadGeneral += publicacion.dificultad
            dominioGeneral += publicacion.dominio
            puntualidadGeneral += publicacion.puntualidad
            asistenciaGeneral += publicacion.asistencia
            seguimientoGeneral += publicacion.seguimiento

        # Calcular promedio de calificaciones generales
        calidadGeneral = round(calidadGeneral / numPublicaciones, 1)
        dificultadGeneral = round(dificultadGeneral / numPublicaciones, 1)
        dominioGeneral = round(dominioGeneral / numPublicaciones, 1)
        puntualidadGeneral = round(puntualidadGeneral / numPublicaciones, 1)
        asistenciaGeneral = round(asistenciaGeneral / numPublicaciones, 1)
        seguimientoGeneral = round(seguimientoGeneral / numPublicaciones, 1)

                
        context['calidadGeneral'] = calidadGeneral
        context['dificultadGeneral'] = dificultadGeneral
        context['dominioGeneral'] = dominioGeneral
        context['puntualidadGeneral'] = puntualidadGeneral
        context['asistenciaGeneral'] = asistenciaGeneral
        context['seguimientoGeneral'] = seguimientoGeneral

        return context

