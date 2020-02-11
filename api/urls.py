from django.urls import path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet,UsuarioList,UsuarioDetalhes

router = routers.DefaultRouter()
router.register('users',UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('usuario/', UsuarioList.as_view()),
    path('usuario/<int:pk>/', UsuarioDetalhes.as_view()),
    
]
