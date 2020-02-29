from rest_framework import serializers
from django.db.models import Q
from conta.models import Account,Perfil,Perfil_Serv
from rest_framework.authtoken.models import Token
class CadastroSerializer( serializers.ModelSerializer ) :

    password2 = serializers.CharField(style ={'input_type' : 'password'}, write_only = True)

    class Meta:
        model = Account
        fields = ['username','email','password','password2','is_staff']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'is_staff' : {'write_only' : True}

        }
   
    def save(self):
        #criando um objeto eu acho
        conta = Account( 
            email = self.validated_data['email'],
            username = self.validated_data['username'],
             is_staff = self.validated_data['is_staff']
        )       
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']


        if password != password2:
            raise serializers.ValidationError({ 'senha' : 'As senhas devem ser iguais.'})
        
        conta.set_password(password)
        conta.save()
        return conta

class LoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(allow_blank = True , read_only = True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField( label = 'Email ',required = False, allow_blank = True)
    # id = serializers.IntegerField()
    
    class Meta:
        model = Account
        fields = ['id','username','email','password','token']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def validate(self,data):
            
            user_obj = None
            email = data.get('email',None)
            username = data.get('username',None)
            password = data['password']

            if not email :
                raise serializers.ValidationError( {"erro" : "um Usuario ou email é obrigatório para o login"})

            usuario = Account.objects.filter (
                Q(email=email) | Q(username = username)
            ).distinct()
            
            usuario = usuario.exclude(email__isnull=True)
            
            if usuario.exists() and usuario.count():
                 user_obj = usuario.first()
                 
                 print(user_obj.id)

            else :
                raise serializers.ValidationError({"erro" : "Usuario ou e-mail inválidos "})

            if user_obj:
                if not user_obj.check_password( password) :
                    raise serializers.ValidationError ( { "erro" : "Credenciais inválidas"})
                
                token = Token.objects.get_or_create(user=user_obj.id)
               
                print(token[0])
                data['id'] = user_obj.id
                data['token']   = token[0] #upla depois converter para lista
                
            return data

class PerfilSerializer(serializers.ModelSerializer):

    class Meta :
        model = Perfil
        fields = '__all__'
class PerfilServSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil_Serv
        fields = '__all__'