from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from django_filters.rest_framework import DjangoFilterBackend


# from django.contrib.auth.models import User
from .serializers import ServicosSerializer,HorarioSerializers,EnderecoSerializers,TelefoneSerializers,ImageSerializer,FavoritosSerializer
# UserSerializer
from servicos.models import Servico,HrFuncionamento,Endereco,Telefone,ImagensServ,Favoritos
from django.views.decorators.csrf import csrf_exempt


from .pagination import PaginacaoUsuario

class ServicosView(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer
class EnderecoServView(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializers
class HorarioView(viewsets.ModelViewSet):
    queryset = HrFuncionamento.objects.all()
    serializer_class = HorarioSerializers
class TelefoneView(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializers

class ImagensServView(viewsets.ModelViewSet):
    queryset = ImagensServ.objects.all()
    serializer_class = ImageSerializer

class FavoritosView(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritosSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields  = ['user','is_active']


@api_view(['GET','PUT','POST'])
def api_favoritos ( request, id,id_s):

    data ={}
    try:
        favoritos = Favoritos.objects.filter(user=id)
        if request.method == 'POST':
            data = request.data
            print("AQUIIIIIIIIIIIIIIIIII@@@@@@@")
            print(data)
            if serializer.is_valid():
                serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        else :    
            print("FAVORITOSS")   
            if request.method == 'GET':
                serializer = FavoritosSerializer(favoritos)
                return Response( serializer.data )
        
            
    except Favoritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    