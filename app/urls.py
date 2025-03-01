from django.urls import path
from . import views

urlpatterns = [
    path('',views.consumo, name ='Filmes'),
    path('search',views.search, name ='search'),
]
