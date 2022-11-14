from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

from django.contrib.auth.models import User
from .models import *
from .util import *
# Create your views here.

def login(request):
    """Campo para a autenticação do usuario"""
    if request.method == 'POST':
        nome_de_usuario = request.POST.get('nome_de_usuario')
        senha = request.POST.get('senha')
        if User.objects.filter(username = nome_de_usuario).exists():
            user = auth.authenticate(request, username = nome_de_usuario, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('redirecionar')
            else:
                messages.error(request, "Senha invalida. Verifique se você digitou sua senha coretamente.")
        else:
            messages.error(request, "Email invalido. Verifique se você digitou seu email coretamente.")    
    return render(request, 'usuario/login.html')

def logout(request):
    """Campo para desconectar um usuario"""
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def Redirecionar(requets):
    return redirect("index_facilitis")


# @login_required(login_url='login')
def cadastro_usuario(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)
    nivel_de_usuario = NivelDeUsuario.objects.all()

    dados = {
        "usuario":usuario_i,
        "tipos_usuarios" : nivel_de_usuario,
    }


    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_n = request.POST['data_n']
        data = datetime.strptime(data_n, '%Y-%m-%d').date()
        nome_u = request.POST.get('user_name')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        nivel_u = request.POST.get('nivel_u')
        nivel_i = get_object_or_404(NivelDeUsuario, pk = nivel_u)
        foto_perfil = request.FILES['foto_perfil']
        campos = [nome, nome_u, senha, senha2]
        for campo in campos:
            if validar_campo_vazio(campo):
                messages.error(request, "Preencha todos os campos corretamente")
                return redirect('cadastro')
            elif validar_nome_de_usuario(nome_u):
                messages.error(request, "Login já existente")
                return redirect('cadastro')
            elif validar_email(email):
                messages.error(request, "Email já cadastrado")
                return redirect('cadastro')
            elif validar_campo_senha(senha, senha2):
                messages.error(request, "Confirmação de Senha não batem")
                return redirect('cadastro')
            elif validar_tipo_usuario(nivel_u):
                messages.error(request, "Selecione o seu nivel de usuario")
                return redirect('cadastro')
            else:
                user = User.objects.create_user(
                    username = nome_u, 
                    email = email, 
                    first_name = nome, 
                    password = senha
                )
                user.save()
                user_id = User.objects.get(email = email)
                user_i = get_object_or_404(User, pk = user_id.id)
                adicional = Usuario.objects.create(
                    usuario = user_i, 
                    telefone = telefone, 
                    nascimento = data, 
                    nivel_de_usuario = nivel_i, 
                    foto_de_perfil = foto_perfil
                )
                adicional.save()
                return redirect('redirecionar')
    return render(request, "usuario/cadastro-de-usuario.html", dados)

def cadastro(request):
    nivel_de_usuario = NivelDeUsuario.objects.all()
    usuario = request.user.id
    usuario_i = get_object_or_404(Usuario, pk = usuario)

    dados = {
        "tipos_usuarios" : nivel_de_usuario,
        "usuario" :usuario_i
    }
    return render(request, 'usuario/teste.html',dados)
