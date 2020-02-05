from rest_framework import serializers
from django.contrib.auth.models import User


#Em teoria estou criando o modelo do retorno do json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only':True ,'required' : True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user