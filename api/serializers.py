from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import * 


# #Em teoria estou criando o modelo do retorno do json
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username','password']
#         extra_kwargs = {'password': {'write_only':True ,'required' : True}}

#     def create(self,validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
# class UsuarioSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Usuario
#         # fields = ['id','nome','email','senha','tel','dt_nasc']
#         fields = '__all__'


class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model =  HrFuncionamento
        fields = '__all__'

    def create(self, validated_data):
        horario = HrFuncionamento.objects.create(**validated_data)
        return horario     
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model : Categoria
        fields : '__all__'   

class ServicosSerializer(serializers.ModelSerializer):
    # servico_horario = serializers.StringRelatedField(many=True)
    # servico_horario = HorarioSerializers(many =True,)
    servico_horario = HorarioSerializers(many=True)
    servico_telefone = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    servico_endereco = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Servico
        # fields =('servico_horario',)
        fields = '__all__'

    def create(self, validated_data):
        horarios_data = validated_data.pop('servico_horario')
        serv = Servico.objects.create(**validated_data)
        for horario_data in horarios_data:
            HrFuncionamento.objects.create(servico=serv, **horario_data)
        return serv   
