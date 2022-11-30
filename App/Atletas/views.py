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
        "atletas":atletas,
        "filtro_posicao" : "Jogadores"
    }

    if request.method == "POST":
        filtro = request.POST['tudo']
        if filtro == "S":
            dados['filtro_posicao'] = "Jogadores"
        elif filtro == "P":
            dados["atletas"] = Atleta.objects.filter(nome__icontains=request.POST['pesquisa'])
        else:
            dados["atletas"] = Atleta.objects.filter(modalidade_id = modalidade_id, posicao_id = filtro)  
            p_i = get_object_or_404(Posicao, pk = filtro)
            dados['filtro_posicao'] = p_i.posicao
            

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
            return redirect('cadastrar_atleta', modalidade.id)

        if Atleta.objects.filter(cpf = cpf).exists():
            messages.error(request, 'Um atleta com esse CPF já foi cadastrado')
            return redirect('cadastrar_atleta', modalidade.id)
        
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

@login_required(login_url="login")
def editar_atleta(request, atleta_id, modalidade_id):
    usuario = request.user.id
    usuario_i = get_object_or_404(Usuario, pk=usuario)
    atleta = get_object_or_404(Atleta, pk=atleta_id)
    data_banco = atleta.data_nascimento
    data = str(data_banco).split(" ")
    posicoes = Posicao.objects.filter(modalidade_id = modalidade_id)

    dados = {
        "usuario":usuario_i,
        "atleta":atleta,
        "data" : data[0],
        "posicoes":posicoes
    }

    if request.method == "POST":
        atleta.nome = request.POST['nome'].strip()
        atleta.apelido = request.POST['apelido']
        atleta.cidade = request.POST['cidade']
        atleta.bairro = request.POST['bairro']
        atleta.endereco = request.POST['endereco']
        atleta.numero_da_casa = request.POST['numero_casa']
        atleta.cep = request.POST['cep']
        atleta.telefone = request.POST['telefone']
        atleta.whatsapp = request.POST['whatsapp']
        atleta.telefone_responsavel = request.POST['telefone_responsavel']
        atleta.telefone_responsavel2 = request.POST['telefone_responsavel2']
        atleta.nome_pai = request.POST['nome_pai']
        atleta.nome_mae = request.POST['nome_mae']
        atleta.altura = request.POST['altura']
        atleta.peso = request.POST['peso']
        atleta.perna_dominante = request.POST['perna_dominante']
        atleta.nivel_escolar = request.POST['nivel_escolar']
        atleta.plano_saude =request.POST['plano_saude']
        atleta.alergia = request.POST['alergia']
        posicao = request.POST['posicao']
        posicao_i = get_object_or_404(Posicao, pk=posicao)
        atleta.posicao = posicao_i
        atleta.camisa = request.POST['camisa']
        atleta.status = request.POST['status']
        print(request.POST['status'])
        atleta.save()
        
        return redirect('visualizar_atleta', atleta.id)


    return render(request, "atletas/editar_atleta.html", dados)

@login_required(login_url="login")
def alterar_foto_atleta(request, atleta_id):
    atleta = get_object_or_404(Atleta, pk=atleta_id)
    if request.method == "POST":
        os.remove(os.path.join(BASE_DIR, atleta.foto_atleta.path))
        atleta.foto_atleta = request.FILES['nova_foto_atleta']
        atleta.save()
        return redirect('visualizar_atleta', atleta.id)
    return redirect('visualizar_atleta', atleta.id)

@login_required(login_url='login')
def listar_jogos(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = Atleta.objects.get(pk=atleta_id)
    jogos = Jogos.objects.filter(atleta_id = atleta).order_by('-criacao')

    dados = {
        "usuario":usuario_i,
        "atleta":atleta,
        "jogos": jogos
    }

    return render(request, 'atletas/listar_jogos.html', dados)

@login_required(login_url='login')
def cadastrar_jogo(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = Atleta.objects.get(pk=atleta_id)
    if request.method == "POST":
        descricao_jogo = request.POST.get("descricao")
        posicao = request.POST.get("posicao")
        minutos_jogados = request.POST.get("minutos")
        gols = request.POST.get("gols")
        finalizacoes = request.POST.get("finalizacoes")
        toques = request.POST.get("toques")
        passes_certos = request.POST.get("passes")

        jogo = Jogos.objects.create(
            atleta = atleta,
            descricao_jogo = descricao_jogo,
            posicao = posicao,
            minutos_jogados = minutos_jogados,
            gols = gols,
            finalizacoes = finalizacoes,
            toques = toques,
            passes_certos = passes_certos
        )

        jogo.save()
    return redirect("listar_jogos", atleta_id)

@login_required(login_url='login')
def visualizar_jogo(request, jogo_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    jogo = Jogos.objects.get(pk = jogo_id)

    dados = {
        "usuario" : usuario_i,
        "jogo" : jogo
    }

    return render(request, 'atletas/jogo_atleta.html', dados)

@login_required(login_url='login')
def relatorio_jogos(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    jogos = Jogos.objects.filter(atleta_id = atleta_id)
    if request.method == "POST":
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        jogos = Jogos.objects.filter(atleta_id = atleta_id).filter(criacao__range = (inicio, fim))

    jogos_d = {
        "Titular" : 0,
        "Minutos Jogados": 0,
        "Gols": 0,
        "Finalizações": 0,
        "Conversão de Gols": 0,
        "Toques": 0,
        "Passes Certos": 0,
        "Porcentagem de Passes" : 0 
    }
    for jogo in jogos:
        if jogo.posicao == "T":
            jogos_d["Titular"] += 1
        jogos_d["Minutos Jogados"] += jogo.minutos_jogados
        jogos_d["Gols"] += jogo.gols
        jogos_d["Finalizações"] += jogo.finalizacoes
        jogos_d["Toques"] += jogo.toques
        jogos_d["Passes Certos"] += jogo.passes_certos
        jogos_d["Conversão de Gols"] += jogo.conversao_de_gols()
        jogos_d["Porcentagem de Passes"] += jogo.porcentagem_de_passes()
    
    if len(jogos) != 0:
        jogos_d["Titular"] = jogos_d["Titular"] / len(jogos)
        jogos_d["Minutos Jogados"] = jogos_d["Minutos Jogados"] / len(jogos)
        jogos_d["Gols"] = jogos_d["Gols"] / len(jogos)
        jogos_d["Finalizações"] = jogos_d["Finalizações"] / len(jogos)
        jogos_d["Toques"] = jogos_d["Toques"] / len(jogos)
        jogos_d["Passes Certos"] = jogos_d["Passes Certos"] / len(jogos)
        jogos_d["Conversão de Gols"] = jogos_d["Conversão de Gols"] / len(jogos)
        jogos_d["Porcentagem de Passes"] = jogos_d["Porcentagem de Passes"] / len(jogos)

    dados = {
        "usuario" : usuario_i,
        "jogos" : jogos_d,
        "atleta" : atleta_id
    }

    return render(request, "atletas/relatorio_jogos.html", dados)


