from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from conta.models import Account
from conta.api.serializers import CadastroSerializer,LoginSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(['POST',])
def cadastro_usuario_view( request ):

    if request.method == 'POST':
        serializer = CadastroSerializer( data = request.data)
        data ={}

        if serializer.is_valid():
            conta = serializer.save()
            data['response'] = 'cadastrado com sucesso'
            data['email'] = conta.email
            data['username'] = conta.username
            token = Token.objects.get(user=conta).key
            data['token'] = token
        else :
            data = serializer.errors

        return Response(data)
        
@api_view(['GET',])
def atualizaToken( request ):
    if request.method =='GET':
        for user in Account.objects.all():
            Token.objects.get_or_create(user=user)
        return JsonResponse( {'mensagem': "Token Atualizado"} ,status = status.HTTP_201_CREATED)   

@api_view(['POST'])
@permission_classes([AllowAny])
def loginUser( request) :
    serializer_class = LoginSerializer

    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid( raise_exception = True ):
            print("View")
            new_data = serializer.data
            return Response( new_data, status = status.HTTP_200_OK )
    return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

@api_view(['GET','POST'])
def soma( request):
    data = {}
    if request.method == 'POST' :
        data = request.data
        data['resultado'] =data['a'] + data['b']
        
    else:
        data ={
            'a': 'passe o valor',
            'b': 'passe o valor',
        }
    return Response(data)

