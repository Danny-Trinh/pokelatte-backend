from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PokemonPostSerializer
from .models import PokemonPost


class PokemonAPIView(viewsets.ModelViewSet):
    serializer_class = PokemonPostSerializer
    queryset = PokemonPost.objects.all()
