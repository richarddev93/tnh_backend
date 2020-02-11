from django.contrib import admin
from .models import *
from functools import partial
from django.forms import MediaDefiningClass
# Register your models here.

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('servico','num')

admin.site.register(Telefone, TelefoneAdmin)

admin.site.register(Servico)
admin.site.register(Usuario)
admin.site.register(UsuarioServ)
# admin.site.register(Telefone)
admin.site.register(Endereco)
admin.site.register(Categoria)