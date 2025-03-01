from rest_framework import serializers
from .models import Usuarios,Filmes

class FilmesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields =  '__all__'

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'