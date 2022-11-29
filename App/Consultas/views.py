from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from App.Usuario.models import Usuario
from App.Atletas.models import Atleta

# Create your views here.

@login_required(login_url='login')
def index_consultas(request):
    usuario = request.user.id
    usuario_i = get_object_or_404(Usuario, usuario_id = usuario)
    atletas = Atleta.objects.all().order_by('nome')
    
    dados = {
        "usuario" : usuario_i,
        "atletas" : atletas
    }

    if request.method == "POST":
        dados["atletas"] = Atleta.objects.filter(nome__icontains=request.POST['pesquisa'])

    return render(request, 'consultas/index_consultas.html', dados)

@login_required(login_url='login')
def visualizar_atleta_consulta(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = get_object_or_404(Atleta, pk=atleta_id)

    dados = {
        "usuario":usuario_i,
        "atleta":atleta
    }

    return render(request, "consultas/visualizar_atleta_consulta.html", dados)

@login_required(login_url='login')
def listar_consultas(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = get_object_or_404(Atleta, pk = atleta_id)
    consultas = Consulta.objects.filter(atleta_id = atleta).order_by('-criacao')
    
    dados = {
        "usuario":usuario_i,
        "consultas":consultas,
        "atleta" :atleta_id,
    }

    return render(request, 'consultas/listar_consultas.html', dados)

@login_required(login_url='login')
def criar_consulta(request, atleta_id):
    atleta = get_object_or_404(Atleta, pk = atleta_id)
    consulta = Consulta.objects.create(atleta = atleta)
    consulta.save()

    return redirect("listar_consultas", atleta_id)

@login_required(login_url='login')
def consulta_geral(request, consulta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    estruturas = EstruturaLesionada.objects.all()
    partes = RegiaoDoCorpo.objects.all()
    exame = ExamesComplementares.objects.all()
    dados = {
        "usuario":usuario_i,
        "consulta":consultas,
        "estruturas": estruturas,
        "partes":partes,
        "exames":exame,
        "entrada":"N",
        "tratamento":"N",
        "complemento":"N",
        "saida":"N",
        "manutencao":"N"
    }
    if Entrada.objects.filter(consulta_id = consultas).exists():
        dados["entrada"] = Entrada.objects.get(consulta_id = consultas)
    else:
        dados["entrada"] = "N"
    if Tratamento.objects.filter(consulta_id = consultas).exists():
        dados["tratamento"] = Tratamento.objects.get(consulta_id = consultas)
    else:
        dados["tratamento"] = "N"
    if ExameTratamento.objects.filter(consulta_id = consultas).exists():
        dados["complemento"] = ExameTratamento.objects.get(consulta_id = consultas)
    else:
        dados["complemento"] = "N"
    if Saida.objects.filter(consulta_id = consultas).exists():
        dados["saida"] = Saida.objects.get(consulta_id = consultas)
    else:
        dados["saida"] = "N"
    if Manutencao.objects.filter(consulta_id = consultas).exists():
        dados["manutencao"] = Manutencao.objects.get(consulta_id = consultas)
    else:
        dados["manutencao"] = "N"
    return render(request, 'consultas/consulta_atleta.html', dados)

@login_required(login_url='login')
def criar_entrada(request, consulta_id):
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    if request.method == "POST":
        estrutura = request.POST['estrutura']
        estrutura_i = get_object_or_404(EstruturaLesionada, pk = estrutura)
        parte = request.POST['parte']
        parte_i = get_object_or_404(RegiaoDoCorpo, pk = parte)
        observacao = request.POST['observacao']
        entrada = Entrada.objects.create(
            consulta = consultas, 
            estrutura_lesionada = estrutura_i,
            regiao_corpo = parte_i,
            observacao = observacao
            )
        entrada.save()
    return redirect("consulta_geral", consulta_id)

@login_required(login_url='login')
def criar_tratamento(request, consulta_id):
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    if request.method == "POST":
        observacao = request.POST['observacao']
        tratamento = Tratamento.objects.create(
            consulta = consultas,
            justificativa = observacao
        )
        tratamento.save()

    return redirect("consulta_geral", consulta_id)

@login_required(login_url='login')
def criar_exame_complementar(request, consulta_id):
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    if request.method == "POST":
        exame = get_object_or_404(ExamesComplementares, pk = request.POST['exame'])
        imagem = request.FILES['image_exame']
        observacao = request.POST['observacao']

        complemento = ExameTratamento.objects.create(
            consulta = consultas,
            exame_complementar = exame,
            imagem_exame = imagem,
            justificativa_complementares = observacao
        )
        

    return redirect("consulta_geral", consulta_id)

@login_required(login_url='login')
def criar_saida(request, consulta_id):
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    if request.method == "POST":
        observacao = request.POST['observacao']
        saida = Saida.objects.create(
            consulta = consultas,
            justificativa = observacao
        )
        saida.save()

    return redirect("consulta_geral", consulta_id)

@login_required(login_url='login')
def criar_manutencao(request, consulta_id):
    consultas = get_object_or_404(Consulta, pk = consulta_id)
    if request.method == "POST":
        tipo_manutencao = request.POST['tipo_manutencao']
        observacao = request.POST['observacao']
        manutencao = Manutencao.objects.create(
            consulta = consultas,
            tipo_manutencao = tipo_manutencao,
            justificativa = observacao
        )
        manutencao.save()

    return redirect("consulta_geral", consulta_id)
    
@login_required(login_url='login')
def visualizar_imagem(request, consulta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    consulta = Consulta.objects.get(pk=consulta_id)
    exame = ExameTratamento.objects.get(consulta_id = consulta.id)

    dados = {
        "usuario":usuario_i,
        "consulta":consulta,
        "exame":exame
    }

    return render(request, 'consultas/consulta_img.html', dados)

@login_required(login_url='login')
def retornar_consulta(request, consulta_id):
    return redirect("consulta_geral", consulta_id)

@login_required(login_url='login')
def relatorio_consulta(request, atleta_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    atleta = Atleta.objects.get(pk=atleta_id)
    consultas = Consulta.objects.filter(atleta_id = atleta)
    count_examen_complementares = 0
    e_lesionadas = EstruturaLesionada.objects.all()
    count_lesionadas = {}
    p_corpos = RegiaoDoCorpo.objects.all()
    count_parte_corpo = {}
    count_manutencao = {
        "Recovery" : 0,
        "Analgesia" : 0,
        "Terapia Manual Osteopatia" : 0,
        "Terapia Manual Manipulação" : 0
    }
    for consulta in consultas:
        if ExameTratamento.objects.filter(consulta_id = consulta).exists():
            count_examen_complementares += 1
        if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "R").exists():
            count_manutencao["Recovery"] += 1
        if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "A").exists():
            count_manutencao["Analgesia"] += 1
        if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "O").exists():
            count_manutencao["Terapia Manual Osteopatia"] += 1
        if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "M").exists():
            count_manutencao["Terapia Manual Manipulação"] += 1
        
    for e_lesionada in e_lesionadas:
        count = Entrada.objects.filter(estrutura_lesionada_id = e_lesionada).count()    
        count_lesionadas[e_lesionada.estrutura_lesionada] = count
    for p_corpo in p_corpos:
        count = Entrada.objects.filter(regiao_corpo_id = p_corpo).count
        count_parte_corpo[p_corpo.parte_do_corpo] = count
    

    if request.method == "POST":
        inicio = request.POST['inicio']
        fim = request.POST['fim']
        count_examen_complementares = 0
        count_manutencao = {
            "Recovery" : 0,
            "Analgesia" : 0,
            "Terapia Manual Osteopatia" : 0,
            "Terapia Manual Manipulação" : 0
        }
        for consulta in consultas:
            if ExameTratamento.objects.filter(consulta_id = consulta).filter(criacao__range = (inicio, fim)).exists():
                count_examen_complementares += 1
            if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "R").filter(criacao__range = (inicio, fim)).exists():
                count_manutencao["Recovery"] += 1
            if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "A").filter(criacao__range = (inicio, fim)).exists():
                count_manutencao["Analgesia"] += 1
            if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "O").filter(criacao__range = (inicio, fim)).exists():
                count_manutencao["Terapia Manual Osteopatia"] += 1
            if Manutencao.objects.filter(consulta_id = consulta).filter(tipo_manutencao = "M").filter(criacao__range = (inicio, fim)).exists():
                count_manutencao["Terapia Manual Manipulação"] += 1

        for e_lesionada in e_lesionadas:
            count = Entrada.objects.filter(estrutura_lesionada_id = e_lesionada).filter(criacao__range = (inicio, fim)).count()    
            count_lesionadas[e_lesionada.estrutura_lesionada] = count
        for p_corpo in p_corpos:
            count = Entrada.objects.filter(regiao_corpo_id = p_corpo).filter(criacao__range = (inicio, fim)).count
            count_parte_corpo[p_corpo.parte_do_corpo] = count

    
        

    dados = {
        "usuario":usuario_i,
        "atleta":atleta,
        "ex_complementares" : count_examen_complementares,
        "count_lesionadas": count_lesionadas,
        "count_partes": count_parte_corpo,
        "count_manutencoes": count_manutencao,
    }

    return render(request, 'consultas/relatorio_consulta.html',dados)