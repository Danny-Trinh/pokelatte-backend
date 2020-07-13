from rest_framework import serializers
from .models import PokemonPost


class PokemonPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonPost
        fields = ('id',
                  'title',
                  'content',
                  'author'
                  )
