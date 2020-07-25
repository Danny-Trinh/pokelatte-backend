from rest_framework import serializers
from .models import PokemonPost, Pokemon
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import token_obtain_pair
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Creation Serializer
    """
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

    def get_token(self, obj):
        token = token_obtain_pair(self, obj)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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
