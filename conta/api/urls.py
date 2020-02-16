from django.urls import path
from conta.api.views import (
    cadastro_usuario_view,
)
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets

# router = routers.DefaultRouter()

# router.register('cadastro',cadastro_usuario_view)

app_name = 'conta'


urlpatterns = [
     path('usuario', cadastro_usuario_view),
]