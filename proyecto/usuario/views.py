from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views
from .forms import RegistroForm

# Create your views here.
class RegistroView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuario:inicio')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = form.save()
        return super().form_valid(form)


class InicioView(views.LoginView):
    template_name = 'usuario/inicio_sesion.html'
    redirect_authenticated_user = True # Redirigir si el usuario ya está autenticado
    next_page = 'publicacion:index' #Pagina a la que redirige

class SalirView(views.LogoutView):
    next_page = 'publicacion:index'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)






