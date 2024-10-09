from django.urls import path, include
from .views import Index, DetalleArticuloView, LikeArticulo, Destacado

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('',Index.as_view(), name='index'),
    path('<int:pk>/', DetalleArticuloView.as_view(), name='detalle_articulo'),
    path('<int:pk>/like', LikeArticulo.as_view(), name='like_articulo'),
    path('destacado', Destacado.as_view(), name='destacado'),
]
