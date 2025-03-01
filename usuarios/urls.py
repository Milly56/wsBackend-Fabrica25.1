from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewsets import UsuarioViewset,FilmesViewset

router = DefaultRouter()
router.register(r'usuarios',UsuarioViewset,basename='usuarios'),
router.register(r'filmes',FilmesViewset,basename='filmes'),

urlpatterns = [
    path('',include(router.urls))
]
