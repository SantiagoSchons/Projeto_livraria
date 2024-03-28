from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["descricao"]
    search_fields = ["descricao"]
