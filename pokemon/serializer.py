from rest_framework import serializers
from .models import PokemonPost, Pokemon


class PokemonPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonPost
        fields = ('id',
                  'title',
                  'content',
                  'author'
                  )


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
