from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *
from .valida import *
from App.Usuario.models import Usuario

@login_required(login_url="login")
def cadastro_funcionario(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)

    dados = {
        "usuario":usuario_i, 
    }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        foto_p = request.FILES['foto_p']
        telefone = request.POST.get('telefone')
        telefone_emergencia = request.POST.get('telefone_emergencia')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        cpf_f = request.FILES['cpf_f']
        rg_f = request.FILES['rg_f']
        funcao = request.POST.get('funcao')
        horario = request.POST.get('horario')
        data_a = request.POST['data_a']
        data = datetime.strptime(data_a, '%Y-%m-%d').date()
        banco = request.POST.get('banco')
        agencia = request.POST.get('agencia')
        conta = request.POST.get('conta')
        pix = request.POST.get('pix')

        if valida_tudo(request, rg, telefone, telefone_emergencia, cep, nome, email, cpf, pix, conta, agencia, banco) == False:
            return redirect('cadastro_funcionario')
        
        funcionario = Funcionario.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            contato_emergencia=telefone_emergencia,
            cep=cep,
            cpf=cpf,
            foto_cpf=cpf_f,
            rg=rg,
            foto_rg=rg_f,
            funcao=funcao,
            endereco=endereco,
            cidade=cidade,
            bairro=bairro,
            uf=uf,
            horario_de_trabalho = horario,
            admitido=data,
            foto_funcionario=foto_p,
            banco=banco,
            agencia=agencia,
            conta=conta,
            pix=pix
        )

        funcionario.save()
        return redirect('redirecionar')
    return render(request, 'funcionario/cadastro_funcionario.html', dados)

        
        
        
        
        


