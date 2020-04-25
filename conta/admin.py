from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from conta.models import Account,Perfil,Perfil_Serv

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'tel','user')
    search_fields = ( 'nome_completo',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Perfil, PerfilAdmin)

class PerfilServAdmin(admin.ModelAdmin):
    list_display = ('user_serv','nome','cpf','telefone','dt_criacao')
    search_fields = ('nome',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Perfil_Serv, PerfilServAdmin)


