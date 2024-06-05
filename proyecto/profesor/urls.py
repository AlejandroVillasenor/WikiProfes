from django.urls import path
from . import views
app_name = 'profesor'
urlpatterns = [
    path('profesor', views.ProfesorView.as_view(), name='profesor'), #/profesor
    path('buscar/', views.ProfesorView.as_view(), name='buscar_profesor'),
    path('perfilProfesor/<int:pk>/', views.PerfilProfesorView.as_view(), name='perfilProfesor')
]