from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Articulo

class Index(ListView):
    model = Articulo
    queryset = Articulo.objects.all().order_by('-fecha')
    template_name = 'blog/index.html'
    paginate_by = 1

class DetalleArticuloView(DetailView):
    model = Articulo
    template_name = 'blog/detalle_articulo.html'