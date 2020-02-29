from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from conta.models import Account,Perfil,Perfil_Serv
from conta.api.serializers import CadastroSerializer,LoginSerializer,PerfilSerializer,PerfilServSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(['POST',])
@permission_classes([AllowAny])
def cadastro_usuario_view( request ):

    if request.method == 'POST':
        serializer = CadastroSerializer( data = request.data)
        print(serializer)
        data ={}

        if serializer.is_valid():
            conta = serializer.save()
            data['response'] = 'cadastrado com sucesso'
            data['email'] = conta.email
            data['id'] = conta.id
            data['username'] = conta.username
            token = Token.objects.get(user=conta).key
            print("Token :"+ token)
            data['token'] = token
        else :
            data = serializer.errors
            print(data)

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

@api_view(['GET','PUT','DELETE','POST'])
def api_perfilUserView( request, id):
    data ={}
    try:
        conta =Account.objects.get(id=id)
        if request.method == 'POST':
            userPerfil = Perfil(user=conta)
        else :       
            userPerfil = Perfil.objects.get(user=conta)
            print(userPerfil)
    except Perfil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerfilSerializer(userPerfil)
        return Response( serializer.data )

    if request.method == 'PUT':
        serializer = PerfilSerializer(userPerfil, data= request.data)
        if serializer.is_valid():
            serializer.save()
            data['success']= "atualizado com sucesso"
            return Response(data=data)
        return Response( serializer.errors ,status=status.HTTP_400_BAD_REQUEST )

    if request.method == 'DELETE':
        operation = userPerfil.delete()
        if operation :
            data['success'] = "deletado com sucesso"
        else:
            data['failure'] = "falha ao deletar"

        return Response ( data=data)

    if request.method == 'POST':
        serializer = PerfilSerializer( userPerfil,data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors ,status=status.HTTP_400_BAD_REQUEST )   


@api_view(['GET','PUT','DELETE','POST'])
def api_perfilServView( request, id):
    data ={}
    try:
        conta_serv =Account.objects.get(id=id)
        if request.method == 'POST':
            userServPerfil = Perfil_Serv(user_serv=conta_serv)
        else :       
            userServPerfil = Perfil_Serv.objects.get(user_serv=conta_serv)
            
    except Perfil_Serv.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerfilServSerializer(userServPerfil)
        return Response( serializer.data )

    if request.method == 'PUT':
        serializer = PerfilServSerializer(userServPerfil, data= request.data)
        if serializer.is_valid():
            serializer.save()
            data['success']= "atualizado com sucesso"
            return Response(data=data)
        return Response( serializer.errors ,status=status.HTTP_400_BAD_REQUEST )

    if request.method == 'DELETE':
        operation = userServPerfil.delete()
        if operation :
            data['success'] = "deletado com sucesso"
        else:
            data['failure'] = "falha ao deletar"

        return Response ( data=data)

    if request.method == 'POST':
        serializer = PerfilServSerializer( userServPerfil,data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors ,status=status.HTTP_400_BAD_REQUEST )   



