from rest_framework import serializers
# from django.contrib.auth.models import User
from servicos.models import HrFuncionamento,Categoria,Servico,Telefone,Endereco

class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model =  HrFuncionamento
        fields = '__all__'

class TelefoneSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Telefone
        fields = '__all__'

class EnderecoSerializers( serializers.ModelSerializer ) :
    class Meta :
        model = Endereco
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model : Categoria
        fields : '__all__'   

class ServicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = '__all__'

