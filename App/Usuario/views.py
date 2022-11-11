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
                return redirect('index')
            else:
                messages.error(request, "Senha invalida. Verifique se você digitou sua senha coretamente.")
        else:
            messages.error(request, "Email invalido. Verifique se você digitou seu email coretamente.")    
    return render(request, 'usuario/login.html')