import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Receita
from .serializers import ReceitaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

    @action(detail=True, methods=['post'])
    def cozinhar(self, request, pk=None):
        receita = self.get_object()
        erros = []

        for item in receita.ingredientes:
            nome = item['nome']
            quantidade = item['quantidade']
            response = requests.post(
                'http://localhost:8001/api/estoque/reduzir/',
                json={'nome': nome, 'quantidade': quantidade}
            )
            if response.status_code != 200:
                erros.append({nome: response.json()})

        if erros:
            return Response({'erros': erros}, status=400)

        return Response({'mensagem': 'Receita cozinhada e estoque atualizado!!'})