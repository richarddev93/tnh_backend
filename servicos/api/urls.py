from django.urls import path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import *
# UserViewSet
router = routers.DefaultRouter()
# router.register('users',UserViewSet)
router.register('servicos',ServicosView)
router.register('enderecos',EnderecoServView)
router.register('horarios',HorarioView)
router.register('telefones',TelefoneView)
router.register('imgs',ImagensServView)
router.register('favoritos',FavoritosView)



urlpatterns = [
    path('', include(router.urls)),
    # path('usuario/', UsuarioList.as_view()),
    # path('usuario/<int:pk>/', UsuarioDetalhes.as_view()),
    path('servicosfavoritos/<int:id>/',api_listFavoritos)
    
]
