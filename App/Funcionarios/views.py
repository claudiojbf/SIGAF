import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from config.settings import BASE_DIR
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

@login_required(login_url="login")
def listar_funcionarios(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    funcionarios = Funcionario.objects.all().order_by('nome')

    dados = {
        "usuario":usuario_i, 
        "funcionarios":funcionarios
    }

    if request.method == "POST":
        pesquisa = request.POST['pesquisa']
        dados["funcionarios"] = Funcionario.objects.filter(nome__icontains = pesquisa)

    return render(request, 'funcionario/listar_funcionarios.html', dados)

@login_required(login_url="login")
def visualizar_funcionario(request, funcionario_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)

    dados = {
        "usuario":usuario_i, 
        "funcionario":funcionario
    }

    return render(request, 'funcionario/visualizar_funcionario.html', dados)

@login_required(login_url="login")
def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    os.remove(os.path.join(BASE_DIR, funcionario.foto_funcionario.path))
    os.remove(os.path.join(BASE_DIR, funcionario.foto_cpf.path))
    os.remove(os.path.join(BASE_DIR, funcionario.foto_rg.path))
    funcionario.delete()

    return redirect("redirecionar")

@login_required(login_url="login")
def editar_funcionario(request, funcionario_id):
    if request.method == 'POST':
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        funcionario.nome = request.POST.get('nome')
        funcionario.email = request.POST.get('email')
        funcionario.telefone = request.POST.get('telefone')
        funcionario.contato_emergencia = request.POST.get('telefone_emergencia')
        funcionario.cep = request.POST.get('cep')
        funcionario.cpf = request.POST.get('cpf')
        funcionario.foto_cpf = request.FILES['cpf_f']
        funcionario.rg = request.POST.get('rg')
        funcionario.foto_rg = request.FILES['rg_f']
        funcionario.funcao = request.POST.get('funcao')
        funcionario.endereco = request.POST.get('endereco')
        funcionario.cidade = request.POST.get('cidade')
        funcionario.bairro = request.POST.get('bairro')
        funcionario.uf = request.POST.get('uf')
        funcionario.horario_de_trabalho = request.POST.get('horario')
        data_a = request.POST['data_a']
        data = datetime.strptime(data_a, '%Y-%m-%d').date()
        funcionario.admitido = data       
        funcionario.foto_funcionario = request.FILES['foto_p']
        funcionario.banco = request.POST.get('banco')
        funcionario.agencia = request.POST.get('agencia')
        funcionario.conta = request.POST.get('conta')
        funcionario.pix= request.POST.get('pix')
        
        funcionario.save()
        return redirect('visualizar_funcionario', funcionario_id)

    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    data_banco = funcionario.admitido
    data = str(data_banco).split(" ")
    dados = {
        "usuario" : usuario_i,
        "funcionario":funcionario,
        "data" : data[0]
    }

    return render (request, 'funcionario/editar_funcionario.html', dados)



        
        
        
        
        


