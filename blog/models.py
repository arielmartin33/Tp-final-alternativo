from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = HTMLField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    destacado = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

   