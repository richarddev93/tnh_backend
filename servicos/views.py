from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

# from django.contrib.auth.models import User
from .serializers import ServicosSerializer,HorarioSerializers,FavoritosSerializer
# UserSerializer
from .models import * 
from django.views.decorators.csrf import csrf_exempt


from .pagination import PaginacaoUsuario

class ServicosView(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer
class HorarioView(viewsets.ModelViewSet):
    queryset = HrFuncionamento.objects.all()
    serializer_class = HorarioSerializers


