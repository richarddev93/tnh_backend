from rest_framework import serializers

from conta.models import Account

class CadastroSerializer( serializers.ModelSerializer ) :

    password2 = serializers.CharField(style ={'input_type' : 'password'}, write_only = True)

    class Meta:
        model = Account
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
   
    def save(self):
        #criando um objeto eu acho
        conta = Account( 
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({ 'senha' : 'As senhas devem ser iguais.'})
        
        conta.set_password(password)
        conta.save()
        return conta