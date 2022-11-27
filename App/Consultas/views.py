from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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