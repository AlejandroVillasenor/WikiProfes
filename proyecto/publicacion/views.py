from typing import Any
from django.db.models.query import QuerySet
from django.views import generic 
from .models import Publicacion
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import PublicacionForm
from .models import Profesor, Materia
from django.shortcuts import render


class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]
        
class CrearPublicacionView(generic.FormView):
    template_name = 'publicacion/crearPublicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('publicacion:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('usuario:inicio')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = Materia.objects.all().order_by('nombre')
        context['profesores'] = Profesor.objects.all().order_by('nombre')
        context['usuario_nombre'] = self.request.user.get_full_name() or self.request.user.username
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(usuario=request.user)
            return redirect(self.success_url)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
