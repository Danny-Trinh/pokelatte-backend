from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from pokemon import views as pokemon_views

router = routers.DefaultRouter()
router.register(r'pokemon', pokemon_views.PokemonAPIView, 'pokemon')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
