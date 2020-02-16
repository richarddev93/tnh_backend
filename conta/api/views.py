from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
        else :
            data = serializer.errors

        return Response(data)

