from django.urls import path, include
from .views import Index, DetalleArticuloView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('',Index.as_view(), name='index'),
    path('<int:pk>/', DetalleArticuloView.as_view(), name='detalle_articulo')
]
