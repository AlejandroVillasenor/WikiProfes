from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    usuarios = models.ManyToManyField('usuario.Usuario', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')

    def __str__(self) -> str:
        return self.nombre