from django.urls import path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet,UsuarioList,UsuarioDetalhes,ServicosView,HorarioView

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('servicos',ServicosView)
router.register('horarios',HorarioView)



urlpatterns = [
    path('', include(router.urls)),
    path('usuario/', UsuarioList.as_view()),
    path('usuario/<int:pk>/', UsuarioDetalhes.as_view()),
    
]

