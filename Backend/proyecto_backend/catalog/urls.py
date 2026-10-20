"""URL configuration for the catalog application."""

from django.urls import path
from . import views

# [Punto 14 - Etapa 1] Rutas internas de la aplicación catalog
urlpatterns = [
    path('', views.catalog_view, name='catalog_index'),
]
