# OpenSuperMarket/nucleo/models.py

from django.db import models

class Mercado(models.Model):
    """
    Modelo para armazenar as informações gerais do mercado.
    """
    nome = models.CharField(max_length=100)
    abertura = models.DateField()
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Mercado"
        verbose_name_plural = "Mercados"