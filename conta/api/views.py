from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from conta.models import Account
from conta.api.serializers import CadastroSerializer


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