from django.shortcuts import render
from django.http import JsonResponse
import json
from chat.models import Projeto

def home(request):
    return render(request, 'chat.html')

def chat(request):
    projetos = Projeto.objects.filter(
        status="andamento"
    )
    nomes = [
        projeto.nome
        for projeto in projetos
    ]
    return JsonResponse({
        "resposta": str(nomes)
    })
