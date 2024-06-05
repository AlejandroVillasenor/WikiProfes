from django.urls import path
from . import views
app_name = 'materia'
urlpatterns = [
    path('materia', views.MateriaView.as_view(), name='materia'), #/materia
    path('buscar/', views.MateriaView.as_view(), name='buscar_materia'),
    path('detalleMateria/<int:pk>/', views.DetalleMateriaView.as_view(), name='detalleMateria')
]