from django.contrib import admin
from django.urls import path

from app_blog.views import (listar_articulos, crear_articulos,buscar_articulo,detalle_articulo,eliminar_articulo,editar_articulo)

urlpatterns = [
    path("articulos/", listar_articulos, name="listar_articulos"),
    path("crear-articulo/", crear_articulos, name="crear_articulos"),
    path("buscar-articulo/", buscar_articulo, name="buscar_articulos"),
    path('detalle_articulo/<int:id>/', detalle_articulo, name='detalle_articulo'),
    path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
]
