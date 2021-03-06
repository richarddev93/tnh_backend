from django.urls import path
from conta.api.views import (
    cadastro_usuario_view,
    atualizaToken,
    loginUser,
    api_perfilUserView,
    api_perfilServView,
    soma
)
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
# router = routers.DefaultRouter()

# router.register('cadastro',cadastro_usuario_view)
app_name = 'conta'

urlpatterns = [
   
     path('usuario', cadastro_usuario_view),
     path('token', atualizaToken),
     path('api-token-auth/', views.obtain_auth_token),
     path('login/',loginUser ,name= 'login'),
     path('perfil/<int:id>/',api_perfilUserView ,name= 'perfil'),
     path('perfils/<int:id>/',api_perfilServView ,name= 'perfil_serv'),
     path('soma/',soma ),

]