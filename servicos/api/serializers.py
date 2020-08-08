from rest_framework import serializers
# from django.contrib.auth.models import User
from servicos.models import HrFuncionamento,Categoria,Servico,Telefone,Endereco,ImagensServ,Favoritos
from cloudinary.templatetags import cloudinary

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
        fields = ('tplograd','lograd','num','compl','bairro','locali','cep','principal','lat','lng')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensServ
        fields = ('id','imagem',)
        
    def to_representation(self, instance):
        representation = super(ImageSerializer, self).to_representation(instance)
        imagemURL = cloudinary.utils.cloudinary_url(instance.imagem.url, width=100, height=150, crop="fill")
        imagemURLx = cloudinary.utils.cloudinary_url(instance.imagem.url, width=100, height=150, crop='fill' , quality="auto:good")
        representation['imagem'] = imagemURLx[0]
        return representation   
            
class ServicosSerializer(serializers.ModelSerializer):
    
    endereco = EnderecoSerializers( many = False, read_only =True)
    categoria = serializers.SlugRelatedField(slug_field='categ_nome',read_only = True,many=True)
    servico_telefone = serializers.StringRelatedField(many=True)
    servico_horario = serializers.StringRelatedField( many = True )
    #imagem_servicos = serializers.StringRelatedField( many = True )
    imagem_servicos = ImageSerializer(many = True,read_only= True)
    class Meta:
        model = Servico
        fields = ('id','nomefantasia','formaspagto','tags','site','email','desc','endereco','categoria','servico_telefone','servico_horario','imagem_servicos','nota_media')



class FavoritosSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Favoritos
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','categ_nome','desc','img',)

    def to_representation(self, instance):
        representation = super(CategoriaSerializer, self).to_representation(instance)
        imagemURLx = cloudinary.utils.cloudinary_url(instance.img.url, width=100, height=150, crop='fill' , quality="auto:good")
        representation['img'] = imagemURLx[0]
        return representation   