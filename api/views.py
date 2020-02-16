from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

# from django.contrib.auth.models import User
from .serializers import UsuarioSerializer,ServicosSerializer,HorarioSerializers
# UserSerializer
from .models import * 
from django.views.decorators.csrf import csrf_exempt


from .pagination import PaginacaoUsuario
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     print(queryset)
#     serializer_class = UserSerializer
    
class UsuarioList(APIView):

    def get(self, request, format=None):
        try:    
            lista_usuario = Usuario.objects.all()
            paginator = PaginacaoUsuario()
            result_page = paginator.paginate_queryset(lista_usuario,request)
            # serializer = UsuarioSerializer(lista_usuario, many=True)
            serializer = UsuarioSerializer(result_page, many=True)
            # return Response(serializer.data)
            return paginator.get_paginated_response(serializer.data)
        except Exception :
            print("Erro")
            return  JsonResponse({'mensagem': "Erro  no Servidor"} ,status = status.HTTP_500_INTERNAL_SERVER_ERROR) 

     # inserir novos registros
    def post(self, request):
        try:
            serializer = UsuarioSerializer(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response( serializer.data ,status = status.HTTP_201_CREATED)
            return  Response( serializer.errors ,status = status.HTTP_400_BAD_REQUEST)

        except Exception :
            return  JsonResponse({'mensagem': "Erro no Servidor"} ,status = status.HTTP_500_INTERNAL_SERVER_ERROR)   

class UsuarioDetalhes(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return JsonResponse({'mensagem':"Usuario não existe."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception :
             return  JsonResponse({'mensagem': "Ocorreu  um erro no Servidor"} ,
                                  status = status.HTTP_500_INTERNAL_SERVER_ERROR) 


    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        serializer = UsuarioSerializer(Usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServicosView(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer
class HorarioView(viewsets.ModelViewSet):
    queryset = HrFuncionamento.objects.all()
    serializer_class = HorarioSerializers
