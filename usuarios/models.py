from django.db import models

class Filmes(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    idade = models.IntegerField()
    
    def __str__(self):
        return f"{self.nome}, {self.categoria}"
    
class Usuarios(models.Model):
    nome = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,blank=True,null=True)
    Filme = models.ManyToManyField(Filmes)

    def __str__(self):
        return f"{self.nome}"
