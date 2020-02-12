from django.urls import path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
<<<<<<< HEAD
from .views import UserViewSet,UsuarioList,UsuarioDetalhes,ServicosView,HorarioView

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('servicos',ServicosView)
router.register('horarios',HorarioView)
=======
from .views import UserViewSet,UsuarioList,UsuarioDetalhes

router = routers.DefaultRouter()
router.register('users',UserViewSet)
>>>>>>> 96814ec98eef11c4aef8058ceb31d7b3a57221b7



urlpatterns = [
    path('', include(router.urls)),
    path('usuario/', UsuarioList.as_view()),
    path('usuario/<int:pk>/', UsuarioDetalhes.as_view()),
    
]
<<<<<<< HEAD

=======
>>>>>>> 96814ec98eef11c4aef8058ceb31d7b3a57221b7
