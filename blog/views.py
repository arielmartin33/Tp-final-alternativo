from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Articulo
from django.shortcuts import get_object_or_404

class Index(ListView):
    model = Articulo
    queryset = Articulo.objects.all().order_by('-fecha')
    template_name = 'blog/index.html'
    paginate_by = 1

class Destacado(ListView):
    model = Articulo
    queryset = Articulo.objects.filter(destacado=True).order_by('-fecha')
    template_name = 'blog/destacado.html'
    paginate_by = 1

class DetalleArticuloView(DetailView):
    model = Articulo
    template_name = 'blog/detalle_articulo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetalleArticuloView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        articulo = Articulo.objects.get(id=self.kwargs.get('pk'))
        if articulo.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context

class LikeArticulo(View):
    def post(self, request, pk):
        articulo = get_object_or_404(Articulo, id=pk)
        user = request.user
        if articulo.likes.filter(pk=user.id).exists():
            articulo.likes.remove(user)
        else:
            articulo.likes.add(user)

            articulo.save()
            return redirect('detalle_articulo', pk=pk)
