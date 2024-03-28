from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from livraria.models import Editora
from livraria.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]
    ordering_fields = ["descricao"]
    ordering = ["descricao"]