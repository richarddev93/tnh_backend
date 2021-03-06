from django.contrib import admin
from .models import *
from functools import partial
from django.forms import MediaDefiningClass


# Register your models here.
class TelefoneInlines(admin.TabularInline):
    model = Telefone
class HorarioInlines(admin.TabularInline):
    model = HrFuncionamento
class EnderecoInlines(admin.StackedInline):
    model = Endereco
    
class ImagensServInlines(admin.StackedInline)    :
    model = ImagensServ
class ServicoAdmin(admin.ModelAdmin):
    inlines = [TelefoneInlines,HorarioInlines,ImagensServInlines]
    # readonly_fields = ('list_telefone',)
    list_display = ('nomefantasia','list_telefone')
    # fields = ('nomefantasia','list_telefone')

    def list_telefone(self,obj):
        telefones = Telefone.objects.filter(servico = obj)
        print(telefones)
        if telefones.count() == 0 :
            return '(None)'
        output = ', '.join([str(tel) for tel in telefones ])
        return output

    list_telefone.short_description = 'Telefone(s)'

admin.site.register(Servico,ServicoAdmin)

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('servico','num')
admin.site.register(Telefone, TelefoneAdmin)

admin.site.register(Endereco)
# admin.site.register(Categoria)
admin.site.register(ImagensServ)

class CategAdmin(admin.ModelAdmin):
    list_display = ('categ_nome','desc')
admin.site.register(Categoria, CategAdmin)

class FavoritosAdmin(admin.ModelAdmin):
    list_display = ('user','servico','is_active')
    search_fields = ( 'nome','servico')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Favoritos, FavoritosAdmin)

