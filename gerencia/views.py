from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .forms import FuncionarioCreationForm, FuncionarioChangeForm, MercadoForm
from autenticacao.models import Funcionario
from nucleo.models import Mercado

def gerencia_index(request):
    """
    View principal da área de gerência. Controla a exibição e manipulação
    de informações do mercado e dos funcionários.
    """
    action = request.GET.get('action', 'edit_mercado')
    context = {'action': action}

    # --- Lógica para Editar Informações do Mercado ---
    if action == 'edit_mercado':
        mercado = Mercado.objects.first()
        if request.method == 'POST':
            form = MercadoForm(request.POST, instance=mercado)
            if form.is_valid():
                form.save()
                messages.success(request, 'Informações do mercado atualizadas com sucesso!')
                return redirect('gerencia_index')
        else:
            form = MercadoForm(instance=mercado)
        context['form_mercado'] = form
        context['mercado'] = mercado

    # --- Lógica para Adicionar Novo Funcionário ---
    elif action == 'add_funcionario':
        if request.method == 'POST':
            form = FuncionarioCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Funcionário adicionado com sucesso!')
                # CORREÇÃO: Construir a URL com o parâmetro
                url_redirecionamento = reverse('gerencia_index') + '?action=edit_funcionario'
                return redirect(url_redirecionamento)
        else:
            form = FuncionarioCreationForm()
        context['form_add_funcionario'] = form

    # --- Lógica para Listar, Editar e Remover Funcionários ---
    elif action == 'edit_funcionario':
        url_redirecionamento = reverse('gerencia_index') + '?action=edit_funcionario'

        if request.method == 'POST' and 'edit_funcionario_submit' in request.POST:
            matricula_edit = request.POST.get('matricula')
            funcionario_instancia = get_object_or_404(Funcionario, pk=matricula_edit)
            form = FuncionarioChangeForm(request.POST, instance=funcionario_instancia)
            if form.is_valid():
                form.save()
                messages.success(request, 'Funcionário atualizado com sucesso!')
                # CORREÇÃO: Redirecionar para a URL construída
                return redirect(url_redirecionamento)

        if request.method == 'POST' and 'remover_funcionario_submit' in request.POST:
            matricula_remov = request.POST.get('matricula_a_remover')
            funcionario_a_remover = get_object_or_404(Funcionario, pk=matricula_remov)
            nome_completo = funcionario_a_remover.get_full_name()
            funcionario_a_remover.delete()
            messages.success(request, f'Funcionário {nome_completo} removido com sucesso!')
            # CORREÇÃO: Redirecionar para a URL construída
            return redirect(url_redirecionamento)

        funcionarios = Funcionario.objects.all().order_by('first_name')
        form_edit_funcionario = FuncionarioChangeForm()

        context['funcionarios'] = funcionarios
        context['form_edit_funcionario'] = form_edit_funcionario

    return render(request, 'gerencia/index.html', context)