from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .util import *
from App.Usuario.models import Usuario
import os
from config.settings import BASE_DIR

# Create your views here.

@login_required(login_url="login")
def AtletaIndex(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    modalidades = Modalidade.objects.all().order_by("id")

    dados = {
        "usuario":usuario_i,
        "modalidades":modalidades
    }

    return render(request, "atletas/index_atletas.html", dados)

@login_required(login_url="login")
def listar_atletas(request, modalidade_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    modalidades = Modalidade.objects.all().order_by("id")
    modalidade_i = get_object_or_404(Modalidade, pk=modalidade_id)
    posicoes = Posicao.objects.filter(modalidade_id = modalidade_id)
    atletas = Atleta.objects.filter(modalidade_id = modalidade_id)

    dados = {
        "usuario":usuario_i,
        "modalidades":modalidades,
        "modalidade_i":modalidade_i,
        "posicoes":posicoes,
        "atletas":atletas
    }

    return render(request, "atletas/listar_atletas.html", dados)

@login_required(login_url="login")
def cadastrar_atleta(request, modalidade_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    posicoes = Posicao.objects.filter(modalidade_id = modalidade_id)
    sub_divisoes = SubDivisao.objects.filter(modalidade_id = modalidade_id)
    modalidade = get_object_or_404(Modalidade, pk=modalidade_id)

    dados = {
        'usuario': usuario_i,
        'posicoes':posicoes,
        'sub_divisoes': sub_divisoes,
        'modalidade' : modalidade
    }

    if request.method == "POST":
        modalidade = get_object_or_404(Modalidade, pk = modalidade_id)
        nome = request.POST['nome'].strip()
        apelido = request.POST['apelido'].strip()
        if apelido == "":
            nome_s = nome.split(" ")
            apelido =nome_s[0]  
        data_nacimento = request.POST['data_nacimento']
        rg = request.POST['rg'].strip()
        if not rg.isdigit():
            messages.error(request, f'RG invalida, porfavor coloque apenas numeros no rg')
            redirect("cadastrar_atleta", modalidade_id)
        cpf = request.POST['cpf'].strip()
        if not validar_documentos(cpf):
            messages.error(request, f'CPF invalido!')
            redirect("cadastrar_atleta", modalidade_id)
        naturalidade_uf = request.POST['naturalidade_uf'].strip()
        cidade = request.POST['cidade'].strip()
        bairro = request.POST['bairro'].strip()
        endereco = request.POST['endereco'].strip()
        numero_casa = request.POST['numero_casa'].strip()
        cep = request.POST['cep'].strip()
        telefone = request.POST['telefone'].strip()
        whatsapp = request.POST['whatsapp'].strip()
        telefone_responsavel = request.POST['telefone_responsavel'].strip()
        telefone_responsavel2 = request.POST['telefone_responsavel2'].strip()
        if telefone_responsavel2 == "":
            telefone_responsavel2 = telefone_responsavel
        nome_pai = request.POST['nome_pai'].strip()
        if nome_pai == "":
            nome_pai = "Não informado"
        nome_mae = request.POST['nome_mae'].strip()
        if nome_mae == "":
            nome_mae = "Não informado"
        peso = request.POST['peso'].strip()
        altura = request.POST['altura'].strip()
        perna_dominante = request.POST['perna_dominante'].strip()
        nivel_escolar= request.POST.get('nivel_escolar').strip()
        alergia = request.POST['alergia'].strip()
        plano_saude = request.POST.get('plano_saude').strip()
        posicao = get_object_or_404(Posicao, pk=request.POST['posicao'])
        image = request.FILES['image']

        # validações para indentificadores (rg, cpf)
        if Atleta.objects.filter(rg = rg).exists():
            messages.error(request, 'Um atleta com esse RG já foi cadastrado')
            return redirect('cadastrodeAtletas')

        if Atleta.objects.filter(cpf = cpf).exists():
            messages.error(request, 'Um atleta com esse CPF já foi cadastrado')
            return redirect('cadastrodeAtletas')
        
        atleta = Atleta.objects.create(
            modalidade = modalidade,
            posicao = posicao,
            nome = nome,
            apelido = apelido,
            data_nascimento = data_nacimento,
            rg = rg,
            cpf = cpf,
            perna_dominante = perna_dominante,
            nivel_escolar = nivel_escolar,
            naturalidade_uf= naturalidade_uf,
            cidade = cidade,
            bairro = bairro,
            endereco = endereco,
            numero_da_casa = numero_casa,
            cep = cep,
            telefone = telefone,
            whatsapp = whatsapp,
            nome_pai = nome_pai,
            nome_mae = nome_mae,
            telefone_responsavel = telefone_responsavel,
            telefone_responsavel2 = telefone_responsavel2,
            altura = altura,
            peso = peso,
            plano_saude = plano_saude,
            alergia = alergia,
            foto_atleta = image
        )

        atleta.save()
        return redirect('redirecionar')
    return render(request, 'atletas/cadastro_atletas.html', dados)

@login_required(login_url="login")
def visualizar_atleta(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = get_object_or_404(Atleta, pk=atleta_id)

    dados = {
        "usuario":usuario_i,
        "atleta":atleta
    }

    return render(request, "atletas/visualizar_atleta.html", dados)

@login_required(login_url="login")
def deletar_atleta(request, atleta_id):
    atleta = get_object_or_404(Atleta, pk=atleta_id)
    os.remove(os.path.join(BASE_DIR, atleta.foto_atleta.path))
    atleta.delete()

    return redirect('redirecionar')