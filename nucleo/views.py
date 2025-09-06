from django.shortcuts import render
from .models import Mercado

def index(request):
    mercado = Mercado.objects.first()
    context = {
        'nome_mercado': mercado.nome if mercado else 'OpenSuperMarket'
    }
    return render(request, 'nucleo/index.html', context)