from django.db import models

# Create your models here.
class Materia(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    usuarios = models.ManyToManyField('usuario.Usuario', through='publicacion.Publicacion')
    profesores = models.ManyToManyField('profesor.Profesor', through='publicacion.Publicacion')

    def __str__(self) -> str:
        return f'{self.clave} - {self.nombre}'