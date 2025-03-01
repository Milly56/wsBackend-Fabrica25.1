from django.shortcuts import render
import requests

chave = "[youkey]"

def consumo(request):
    filme = request.GET.get('filme', 'Harry Potter')
    url = f"https://www.omdbapi.com/?t={filme}&apikey={chave}"
    response = requests.get(url)

    if response.status_code == 200:
        fim = response.json()
        return render(request,'filmes.html',{'fim':fim})

def search(request):
    return render(request,'buscar.html')




