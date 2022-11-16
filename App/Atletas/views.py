from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .util import *
from App.Usuario.models import Usuario

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
def visualizar_atletas(request, modalidade_id):
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

    return render(request, "atletas/visualizar_atletas.html", dados)

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
        sub = get_object_or_404(SubDivisao, pk = request.POST.get('subdivisao'))
        modalidade = get_object_or_404(Modalidade, pk = modalidade_id)
        nome = request.POST['nome']
        apelido = request.POST['apelido']
        posicao = get_object_or_404(Posicao, pk=request.POST['posicao'])
        data_nacimento = request.POST['data_nacimento']
        rg = request.POST['rg']
        cpf = request.POST['cpf']
        perna_dominante = request.POST['perna_dominante']
        naturalidade_uf = request.POST['naturalidade_uf']
        cidade = request.POST['cidade']
        endereco = request.POST['endereco']
        numero_casa = request.POST['numero_casa']
        bairro = request.POST['bairro']
        cep = request.POST['cep']
        telefone = request.POST['telefone']
        whatsapp = request.POST['whatsapp']
        whatsapp2 = request.POST['whatsapp2']
        nome_pai = request.POST['nome_pai']
        nome_mae = request.POST['nome_mae']
        telefone_responsavel = request.POST['telefone_responsavel']
        telefone_responsavel2 = request.POST['telefone_responsavel2']
        peso = request.POST['peso']
        altura = request.POST['altura']
        image = request.FILES['image']

        if 'semalergia' in request.POST:
            alergia = 'nulo'
        if 'alergia' in request.POST:
            alergia = request.POST['alergia'].lstrip()
            if valida_campo_vazio(alergia):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo alergia. marque Não tenho alergia para caso ele não exista')
                return redirect('cadastrodeAtletas')
        
        # validações para informações sobre o plamo de saude
        if 'semPlanoSaude' in request.POST:
            plano_saude = 'nulo'
        
        if 'plano_saude' in request.POST:
            plano_saude = request.POST['plano_saude'].lstrip()
            if valida_campo_vazio(plano_saude):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo plano de saude. marque Não tenho plano de saúde para caso ele não existir')
                return redirect('cadastrodeAtletas')
        
        # validações para informações sobre escolaridade
        if 'sem_escolaridade' in request.POST:
            matricula_escolar = 'nulo'
            serie = 'nulo'
            nivel_escolar='nulo'
            
        if 'matricula_escolar' and 'serie' and 'nivel_escolar' in request.POST:
            matricula_escolar = request.POST['matricula_escolar'].lstrip()
            serie = request.POST['serie'].lstrip()
            nivel_escolar =  request.POST['nivel_escolar']
            campos = [request.POST['matricula_escolar'], request.POST['serie']]
            nomes = ['matricula escolar','serie' ]
            iterador = -1
            for campo in campos:
                iterador = iterador+1
                if valida_campo_vazio(campo):
                    messages.error(request, f'O caractere espaço não e considerado no começo do campo {nomes[iterador]} ou marque sem escolaridade')
                    return redirect('cadastrodeAtletas')

        # validações para indentificadores (rg, cpf)
        if Atleta.objects.filter(rg = rg).exists():
            messages.error(request, 'Um atleta com esse RG já foi cadastrado')
            return redirect('cadastrodeAtletas')

        if Atleta.objects.filter(cpf = cpf).exists():
            messages.error(request, 'Um atleta com esse CPF já foi cadastrado')
            return redirect('cadastrodeAtletas')
        
        campos = [request.POST['nome'], request.POST['apelido'], request.POST['naturalidade_uf'], request.POST['cidade'], 
        request.POST['endereco'],request.POST['cpf'], request.POST['cep'],request.POST['nome_pai'],request.POST['nome_mae'],
        request.POST['bairro'],]
        nomes = ['nome', 'apelido', 'naturalidade','cidade','endereco','CPF', 'CEP','nome do pai','nome da mãe','bairro' ]
        iterador = -1
        for campo in campos:
            iterador = iterador+1
            if valida_campo_vazio(campo):
                messages.error(request, f'preencha os campos coretamente, o caractere espaço não e considerado no começo do campo {nomes[iterador]}')
                return redirect('cadastrodeAtletas')
        
        atleta = Atleta.objects.create(
            modalidade = modalidade,
            posicao = posicao,
            nome = nome,
            apelido = apelido,
            data_nascimento = data_nacimento,
            cpf = cpf,
            perna_dominante = perna_dominante,
            matricula_escolar = matricula_escolar,
            serie = serie,
            nivel_escolar = nivel_escolar,
            naturalidade_uf= naturalidade_uf,
            cidade = cidade,
            bairro = bairro,
            endereco = endereco,
            numero_da_casa = numero_casa,
            cep = cep,
            telefone = telefone,
            whatsapp = whatsapp,
            whatsapp2 = whatsapp2,
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