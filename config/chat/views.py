from django.shortcuts import render
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'chat.html')

def chat(request):
    body = json.loads(
        request.body
    )
    mensagem = body["mensagem"]
    return JsonResponse({
        "resposta":
        f"Você disse: {mensagem}"
    })