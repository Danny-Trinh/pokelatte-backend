from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PokemonSerializer
from .models import Pokemon


class PokemonAPIView(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
