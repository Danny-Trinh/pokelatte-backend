from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import PokemonSerializer
from .models import Pokemon


class PokemonAPIView(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    # permision_classes = [
    #     permissions.IsAuthenticated
    # ]

    # def get_queryset(self):
    #     return self.request.user.pokemons.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
