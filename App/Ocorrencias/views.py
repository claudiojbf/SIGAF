from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from App.Usuario.models import Usuario

# Create your views here.
@login_required(login_url='login')
def IndexFacilities(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    ocorrencias = Ocorrencia.objects.all()
    o_abertos = Ocorrencia.objects.filter(status="ABT").count()
    o_em_andamento = Ocorrencia.objects.filter(status="EA").count()
    o_concluido = Ocorrencia.objects.filter(status="C").count()

    dados = {
        "usuario":usuario_i,
        "ocorrencias":ocorrencias,
        "aberto":o_abertos,
        "andamento":o_em_andamento,
        "concluido":o_concluido  
    }
    return render(request, "facilitis/index_facilitis.html", dados)