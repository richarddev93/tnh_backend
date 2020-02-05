from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome            = models.CharField( max_length = 100 )
    usuario_serv    = models.CharField( max_length = 8 )
    senha   = models.CharField( max_length = 8 )
    email_usuario = models.CharField( max_length = 60 ) 
    cpf        = models.CharField( max_length = 11 )
    telefone      = models.CharField( max_length = 11 )


    def __str__(self):
        return self.name


class Telefone(models.Model):
    ddd = models.CharField( max_length = 2 )
    num = models.CharField( max_length = 9 )
    wp  = models.CharField( max_length = 1 )
    principal = models.CharField( max_length = 1)
    servico = ()

    def __str__(self):
        return self.num

class Categoria(models.Model):
    categ_nome = models.CharField(max_length=10 )
    principal  = models.CharField( max_length=2 )
  
    def __str__(self):
        return self.categ_name

class HrFuncionamento ( models.Model ):
    dia = models.CharField( max_length = 9 )
    horario =models.CharField( max_length = 60 )

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
    gia      = models.CharField( max_length = 4 )
    unidade  = models.CharField( max_length = 4 )
    ibge     = models.CharField( max_length = 4 )
               
class Servico(models.Model):
    nomefantasia = models.CharField( max_length = 60)
    razaosocial  = models.CharField( max_length = 60,blank = True, null = True)
    cnpj = models.CharField( max_length=14, blank = True, null = True)
    formaspagto = models.CharField( max_length = 14 )
    tags = models.CharField( max_length = 100 )
    site = models.CharField( max_length = 100 )
    email  = models.EmailField( max_length = 100)
    image = models.ImageField( upload_to='profile_picture', blank = True, null = True)
    desc  = models.TextField( max_length=200 )

    usuario  = models.ForeignKey(Usuario,on_delete = models.CASCADE)
    endereco = models.ManyToManyField(Endereco)
    horario  = models.ManyToManyField(Telefone) 

   

    def __str__(self):
        return self.nomefantasia



 

