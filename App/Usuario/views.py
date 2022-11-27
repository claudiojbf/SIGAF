from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
import os
from config.settings import BASE_DIR

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
    usuario = requets.user.id
    nivel_de_usuario = get_object_or_404(Usuario, usuario_id = usuario)
    if nivel_de_usuario.nivel_de_usuario.sigla == "FAC":
        return redirect("index_facilitis")
    elif nivel_de_usuario.nivel_de_usuario.sigla == "GES":
        return redirect("index_atleta")
    elif nivel_de_usuario.nivel_de_usuario.sigla == "PRF":
        return redirect("index_consultas")


@login_required(login_url='login')
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

@login_required(login_url='login')
def perfil(request):
    usuario = request.user.id
    usuario_i = Usuario.objects.get(usuario_id = usuario)

    dados = {
        "usuario" : usuario_i,
    }

    return render(request, "usuario/perfil.html" ,dados)

@login_required(login_url='login')
def alterar_senha(request):
    usuario = request.user.id
    usuario_i = get_object_or_404(User, pk=usuario)
    if request.method == "POST":
        senha_antiga = request.POST['senha_antiga']
        senha_nova = request.POST['senha_nova'].strip()
        senha_nova2 = request.POST['senha_nova2'].strip()
        print(senha_antiga, senha_nova, senha_nova2, usuario_i.check_password(senha_antiga))
        if usuario_i.check_password(senha_antiga):
            if senha_nova == senha_nova2 and len(senha_nova) > 4:
                usuario_i.set_password(senha_nova)
                usuario_i.save()
                messages.success(request, "Senha Alterada com sucesso!")
                return redirect("perfil")
            else:
                messages.error(request, "Verifique se você esta digitando a senha corretamente,a senha tem que ser maior que 4 digitos.")
                return redirect("perfil")
        else:
            messages.error(request, "Senha antiga incorreta!")
            return redirect("perfil")
    return redirect("perfil")

@login_required(login_url='login')
def alterar_foto_perfil(request):
    usuario = request.user.id
    usuario_i = get_object_or_404(Usuario, usuario_id=usuario)

    if request.method == "POST":
        os.remove(os.path.join(BASE_DIR, usuario_i.foto_de_perfil.path))
        usuario_i.foto_de_perfil = request.FILES['nova_foto_perfil']
        print(request.FILES['nova_foto_perfil'])
        usuario_i.save()

    return redirect("perfil")

@login_required(login_url='login')
def alterar_dados(request):
    usuario = request.user.id
    usuario_i = get_object_or_404(Usuario, usuario = usuario)
    user_i = get_object_or_404(User, pk=usuario)
    if request.method == "POST":
        user_i.first_name = request.POST.get('nome')
        user_i.email = request.POST.get('email')
        user_i.save()
        usuario_i.telefone = request.POST.get('telefone')
        usuario_i.save()
        return redirect("perfil")
    return redirect("perfil")
