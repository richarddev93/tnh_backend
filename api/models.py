from django.db import models

# Create your models here.

class UsuarioServ(models.Model):
    nome            = models.CharField( max_length = 100 )
    usuario_serv    = models.CharField( max_length = 8 )
    senha   = models.CharField( max_length = 8 )
    email_usuario = models.CharField( max_length = 60 ) 
    cpf        = models.CharField( max_length = 11 )
    telefone      = models.CharField( max_length = 11 )
    dt_criacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome


class Telefone(models.Model):
    ddd = models.CharField( max_length = 2 )
    num = models.CharField( max_length = 9 )
    wp  = models.CharField( max_length = 1 )
    principal = models.CharField( max_length = 1)
    servico = models.ForeignKey('Servico', related_name='servico_telefone', on_delete=models.CASCADE)

    def __str__(self):
        return self.num

class Categoria(models.Model):
    categ_nome = models.CharField(max_length=10 )
    principal  = models.CharField( max_length=2 )

  
    def __str__(self):
        return self.categ_nome

class HrFuncionamento ( models.Model ):
    dia = models.CharField( max_length = 9 )
    horario =models.CharField( max_length = 60 )
    servico = models.ForeignKey('Servico', related_name='servico_horario', on_delete=models.CASCADE)

    def __str__(self):
        return self.dia
    
class Endereco(models.Model):
    tpLograd = models.CharField( max_length = 3  )
    lograd   = models.CharField( max_length = 40 )
    num      = models.IntegerField()
    compl    = models.CharField( max_length = 25 )
    bairro   = models.CharField( max_length = 20 )
    locali   = models.CharField( max_length = 30 )
    cep      = models.CharField( max_length = 8 )
    uf       = models.CharField( max_length = 2 )
    gia      = models.CharField( max_length = 4 ,blank=True ,null=True )
    unidade  = models.CharField( max_length = 4, blank=True, null=True )
    ibge     = models.CharField( max_length = 4 ,blank=True, null=True )
    servico = models.ForeignKey('Servico', related_name='servico_endereco', on_delete=models.CASCADE)
               
class Servico(models.Model):
    nomefantasia = models.CharField( max_length = 60)
    razaosocial  = models.CharField( max_length = 60,blank = True, null = True)
    cnpj = models.CharField( max_length=14, blank = True, null = True)
    formaspagto = models.CharField( max_length = 100 )
    tags = models.CharField( max_length = 100 )
    site = models.CharField( max_length = 100 )
    email  = models.EmailField( max_length = 100)
    image = models.ImageField( upload_to='profile_picture', blank = True, null = True)
    desc  = models.TextField( max_length=200 )
    nota_media = models.DecimalField(max_digits = 3,decimal_places=2 ,editable=False,default=0)

    usuario  = models.ForeignKey( UsuarioServ ,on_delete = models.CASCADE)
    # endereco = models.ManyToManyField( Endereco)
    # telefone  = models.ManyToManyField( Telefone) 
    categoria = models.ManyToManyField( Categoria)
    status  = models.BooleanField(default=True)
    horario = models.CharField(max_length=60)


    def __str__(self):
        return self.nomefantasia


class Avaliacao(models.Model) :
    nota = models.IntegerField()
    comentario = models.TextField( max_length=200 )
    id_usuario_consum = models.IntegerField()
    id_servico = models.IntegerField()

class Usuario(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField( max_length=100)
    senha = models.CharField(max_length=8)
    tel=models.CharField(blank=True,null=True,max_length=15)
    foto=models.ImageField(upload_to='profile_picture',blank=True,null=True)
    dt_nasc=models.DateField(blank=True,null=True)
    #endereço
    tpLograd = models.CharField( max_length = 3  )
    lograd   = models.CharField( max_length = 40 )
    num      = models.IntegerField()
    compl    = models.CharField( max_length = 25 )
    bairro   = models.CharField( max_length = 20 )
    locali   = models.CharField( max_length = 30 )
    cep      = models.CharField( max_length = 8 )
    uf       = models.CharField( max_length = 2 )
    
    dt_criacao = models.DateTimeField(auto_now_add=True,blank=False,null=False)

    def __str__(self):
        return self.nome
        
    


 

