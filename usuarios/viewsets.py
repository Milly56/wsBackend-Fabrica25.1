
from .serializers import UsuariosSerializers, FilmesSerializers
from rest_framework import viewsets
from .models import Usuarios, Filmes

class FilmesViewset(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializers

class UsuarioViewset(viewsets.ModelViewSet):
  queryset = Usuarios.objects.all()
  serializer_class = UsuariosSerializers

