from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from autenticacao.models import Funcionario, Funcao
from nucleo.models import Mercado

class FuncionarioCreationForm(UserCreationForm):
    funcoes = forms.ModelMultipleChoiceField(
        queryset=Funcao.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cargos"
    )

    class Meta(UserCreationForm.Meta):
        model = Funcionario
        fields = ('username', 'first_name', 'last_name', 'email', 'nascimento', 'cpf', 'funcoes')
        labels = {
            'username': 'Nome de Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'nascimento': 'Data de Nascimento',
        }


class FuncionarioChangeForm(UserChangeForm):
    password = None
    funcoes = forms.ModelMultipleChoiceField(
        queryset=Funcao.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cargos"
    )

    class Meta(UserChangeForm.Meta):
        model = Funcionario
        fields = ('username', 'first_name', 'last_name', 'email', 'nascimento', 'cpf', 'funcoes', 'is_active', 'is_staff')
        labels = {
            'username': 'Nome de Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'nascimento': 'Data de Nascimento',
            'is_active': 'Ativo',
            'is_staff': 'Acesso à Gerência',
        }

class MercadoForm(forms.ModelForm):
    class Meta:
        model = Mercado
        fields = ('nome', 'abertura', 'cnpj')
        labels = {
            'nome': 'Nome do Mercado',
            'abertura': 'Data de Abertura',
        }