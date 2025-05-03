from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingrediente
from .serializers import IngredienteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    @action(detail=False, methods=['post'])
    def reduzir(self, request):
        nome = request.data.get('nome')
        quantidade = int(request.data.get('quantidade', 0))

        try:
            ingrediente = Ingrediente.objects.get(nome=nome)
            if ingrediente.quantidade >= quantidade:
                ingrediente.quantidade -= quantidade
                ingrediente.save()
                return Response({'status': 'Ingrediente reduzido'})
            else:
                return Response({'erro': 'Quantidade insuficiente'}, status=400)
        except Ingrediente.DoesNotExist:
            return Response({'erro': 'Ingrediente não encontrado'}, status=404)