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
    consultas = Consulta.objects.filter(atleta_id = atleta)
    
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
    entrada = Entrada.objects.get(consulta_id = consultas).exists()
    print(entrada)

    dados = {
        "usuario":usuario_i,
        "consulta":consultas,
    }

    return render(request, 'consultas/consulta_atleta.html', dados)