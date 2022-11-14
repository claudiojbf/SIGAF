from django.shortcuts import render, redirect, get_object_or_404
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

@login_required(login_url='login')
def filtro_status(request, status):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    if status == 1:
        ocorrencias = Ocorrencia.objects.filter(status="ABT")
    elif status == 2:
        ocorrencias = Ocorrencia.objects.filter(status="EA")
    elif status == 3:
        ocorrencias = Ocorrencia.objects.filter(status="C")
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
    return render(request, "facilitis/ocorrencia/index_facilitis_status.html", dados)


@login_required(login_url="login")
def visualizar_ocorrencia(request, ocorrencia_id):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    dados = {
        "ocorrencia": ocorrencia,
        "usuario": usuario_i 
    }

    return render(request, 'facilitis/ocorrencia/visualizar_ocorrencia.html', dados)

@login_required(login_url="login")
def alterar_status_ocorrencia(request, ocorrencia_id, status):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    if status == 1:
        ocorrencia.status = "ABT"
    elif status == 2:
        ocorrencia.status = "EA"
    elif status == 3:
        ocorrencia.status = "C"
    ocorrencia.save()

    return redirect("visualizar_ocorrencia", ocorrencia_id)

@login_required(login_url="login")
def cadastrar_ocorrencia(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    locals = Local.objects.all()
    dados = {
        "usuario" : usuario_i,
        "locals" : locals 
    }

    if request.method == "POST":
        local = request.POST.get('local')
        local_i = get_object_or_404(Local, pk=local)
        titulo_da_ocorrencia = request.POST.get('titulo_da_ocorrencia')
        descricao_da_ocorrencia = request.POST.get('descricao_da_ocorrencia')
        ocorrencia = Ocorrencia.objects.create(
        local = local_i, 
        titulo_da_ocorrencia = titulo_da_ocorrencia, 
        descricao_da_ocorrencia = descricao_da_ocorrencia,
        usuario = usuario_i 
        )
        
        ocorrencia.save()

        return redirect("redirecionar")
    return render(request, 'facilitis/ocorrencia/cadastro_de_ocorrencia.html', dados)

    
@login_required(login_url="login")
def deletar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    ocorrencia.delete()

    return redirect("redirecionar")

@login_required(login_url="login")
def editar_ocorrencia(request, ocorrencia_id):
    if request.method == 'POST':
        ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
        ocorrencia.titulo_da_ocorrencia = request.POST.get('titulo_da_ocorrencia')
        ocorrencia.descricao_da_ocorrencia = request.POST.get('descricao_da_ocorrencia')
        ocorrencia.save()
        return redirect('visualizar_ocorrencia', ocorrencia_id)

    
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    dados = {
        "usuario" : usuario_i,
        "ocorrencia":ocorrencia,
    }

    return render (request, 'facilitis/ocorrencia/editar_ocorrencia.html', dados)