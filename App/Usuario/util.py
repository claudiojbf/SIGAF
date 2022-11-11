from django.shortcuts import redirect, get_object_or_404
from .models import User

def validar_campo_vazio(valor):
    return not valor.strip()

def validar_campo_senha(senha, senha2):
    return senha != senha2

def validar_nome_de_usuario(valor):
    return User.objects.filter(username = valor).exists()

def validar_email(valor):
    return User.objects.filter(email = valor).exists()

def validar_tipo_usuario(valor):
    return valor == "err"