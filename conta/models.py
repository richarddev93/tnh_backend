
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from cloudinary.models import CloudinaryField
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None,is_staff=False):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not is_staff:
			raise ValueError('Users must have a staff')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			is_staff = is_staff,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password, is_staff):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			is_staff = is_staff,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','is_staff',]

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



class Perfil(models.Model):
   
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        unique=True,
    )
    nome_completo = models.CharField(max_length=60)
    tel=models.CharField(blank=True,null=True,max_length=15)
    foto=CloudinaryField(blank=True,null=True)
    dt_nasc=models.DateField(blank=True,null=True)
    genero = models.CharField( max_length= 1,blank=True, null=True)
    interesses = models.CharField ( max_length=100)
    promos = models.CharField( max_length = 1,default='N')
    favoritos = models.CharField(max_length = 100,blank=True, null=True)
    #endereço
    tplograd = models.CharField( max_length = 3  )
    lograd   = models.CharField( max_length = 40 )
    num      = models.IntegerField()
    compl    = models.CharField( max_length = 25 )
    bairro   = models.CharField( max_length = 20 )
    locali   = models.CharField( max_length = 30 )
    cep      = models.CharField( max_length = 8 )
    uf       = models.CharField( max_length = 2 )
    

    def __str__(self):
        return self.nome_completo


@receiver(post_save ,sender = settings.AUTH_USER_MODEL)
def create_auth_token( sender, instance = None, created = False, **kwargs):
    if created :
        Token.objects.create( user = instance )


class Perfil_Serv(models.Model):
    
    user_serv  = models.ForeignKey(Account,on_delete=models.CASCADE,unique=True )
    nome       = models.CharField( max_length = 100 )
    cpf        = models.CharField( max_length = 11 )
    telefone   = models.CharField( max_length = 11 )
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
