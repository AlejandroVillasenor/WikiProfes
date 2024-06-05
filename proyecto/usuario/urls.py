from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistroView.as_view(), name='registro'), #/registro
    path('inicio', views.InicioView.as_view(), name='inicio'), #/inicio
    path('salir', views.SalirView.as_view(), name='salir'), #/salir
]