from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Funcionario, Funcao

class FuncionarioAdmin(UserAdmin):
    # Adiciona os campos customizados ao painel de admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais', {'fields': ('nascimento', 'cpf', 'funcoes')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nascimento', 'cpf', 'funcoes')}),
    )

# Registra os modelos para que apareçam no admin
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Funcao)