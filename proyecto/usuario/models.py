from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre_usuario = models.CharField(max_length=20)
    profesores = models.ManyToManyField('profesor.Profesor', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')