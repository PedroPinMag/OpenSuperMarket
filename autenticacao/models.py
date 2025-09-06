# OpenSuperMarket/autenticacao/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Funcao(models.Model):
    """
    Modelo para armazenar as funções que um funcionário pode ter.
    """
    NOME_CHOICES = (
        ('caixa', 'Caixa'),
        ('financeiro', 'Financeiro'),
        ('gerente', 'Gerente'),
    )
    nome = models.CharField(max_length=20, choices=NOME_CHOICES, unique=True)

    def __str__(self):
        return self.get_nome_display()


class Funcionario(AbstractUser):
    """
    Modelo de funcionário customizado, estendendo o usuário padrão do Django.
    """
    # Removemos o default=gerar_matricula e tornamos o campo não editável e permitimos que seja nulo temporariamente
    matricula = models.CharField(max_length=12, unique=True, primary_key=True, editable=False)
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    funcoes = models.ManyToManyField(Funcao, blank=True)

    def save(self, *args, **kwargs):
        # Gera a matrícula apenas se o funcionário for novo (não tiver matrícula ainda)
        if not self.matricula:
            hoje = datetime.date.today()
            prefixo = hoje.strftime('%Y%m%d')
            # Busca o último funcionário criado hoje para gerar o sequencial
            ultimo_funcionario = Funcionario.objects.filter(matricula__startswith=prefixo).order_by('matricula').last()

            if ultimo_funcionario:
                # Pega os últimos 4 dígitos da matrícula e incrementa
                sequencial = int(ultimo_funcionario.matricula[-4:]) + 1
            else:
                # Se for o primeiro do dia, o sequencial é 1
                sequencial = 1

            self.matricula = f'{prefixo}{sequencial:04d}'
        super().save(*args, **kwargs)  # Salva o objeto no banco de dados

    def __str__(self):
        return self.get_full_name() or self.username