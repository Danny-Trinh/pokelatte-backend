from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status, permissions
from .serializer import PokemonSerializer
from .models import Pokemon

from .serializer import UserSerializer


class UserCreateView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PokemonAPIView(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    # queryset = Pokemon.objects.all()

    def get_queryset(self):
        return Pokemon.objects.filter(trainer=self.request.user.id)

# not needed anymore, but shows how to decode a jwt token
# def dispatch(self, request, *args, **kwargs):
#     if('Authorization' in request.headers):
#         encoded = request.headers['Authorization']
#         encoded = encoded[4:]
#         decoded = jwt.decode(encoded, None, None)
#         print(decoded)
#     return super().dispatch(request, *args, **kwargs)
#   def decode_jwt(str):
#     return jwt.decode(str.split(' ')[1])


def HomeView(request):
    return render(request, 'pokemon/home.html')
