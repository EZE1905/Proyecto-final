from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):
    # atributos de articulos
    titulo = models.CharField(max_length = 200)
    subtitulo = models.CharField(max_length = 300, null=True, blank=True)
    cuerpo = models.TextField(null=False)
    autor = models.CharField(max_length = 100)
    fecha =  models.DateField(null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
