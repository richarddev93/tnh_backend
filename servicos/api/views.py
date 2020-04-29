from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

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


@api_view(['GET'])
def api_listFavoritos ( request, id):

    data ={}
    try:        
        print("123456")
        favoritos = Favoritos.objects.values('servico').filter(
        Q(user = id),
        Q(is_active = True))

        if favoritos :
            servsFavoritos = Servico.objects.raw('select a.* from servicos_servico a inner join servicos_favoritos b on b.Servico_id = a.id where b.user_id ='+str(id))       
            if request.method == 'GET':
                serializer = ServicosSerializer(servsFavoritos,many=True)                                  
                print( serializer.data)
                return Response( serializer.data )

    except Favoritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   


    