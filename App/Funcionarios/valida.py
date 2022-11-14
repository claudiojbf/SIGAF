from validate_docbr import CPF
import re
from django.contrib import messages
from .models import Funcionario


def cpf_valido(numero_do_cpf):      
    cpf = CPF()  
    return cpf.validate(numero_do_cpf)

def valida_campo_vazio(valor):
    return not valor.strip()

def rg_valido(rg):
    return len(rg) > 8

def numero_cartao_valido(numero_cartao):
    return len(numero_cartao) == 16 

def cvv_valido(cvv):
    return len(cvv) == 3 and cvv.isdigit()

def nomes_valido(nome):
    novo_nome = nome.replace(" ","")
    return novo_nome.isalpha() 

def cep_valido(cep):
    modelo = '[0-9]{5}[0-9]{3}'
    resposta = re.findall(modelo, cep)
    return resposta

def telefone_valido(numero_celular):
    return len(numero_celular) == 11

def emal_valido(email):
    modelo = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    resposta = re.findall(modelo, email)
    return resposta
def valida_tudo(request,rg,telefone,telefone_emergência,cep,nome,email,cpf, pix,conta,agencia,banco):
    validacao = True
    if not cpf_valido(cpf):
        messages.error(request, 'o numero do CPF esta inconcistente ')
        validacao = False
    if not rg_valido(rg):
        messages.error(request, 'o numero do RG deve conter no minimo 9 digitos ')
        validacao = False

    if not telefone_valido(telefone):
        messages.error(request, 'o numero do telefone deve seguir o modelo 11912341234! ')
        validacao = False
    if not telefone_valido(telefone_emergência):
        messages.error(request, 'o numero do telefone deve seguir o modelo 11912341234!')
        validacao = False  

    # if not numero_cartao_valido(conta):
    #     messages.error(request, 'o numero do cartão deve seguir o modelo xxxx xxxx xxxx xxxx ')
    #     validacao = False 

    if not cep_valido(cep):
        messages.error(request, 'o CEP deve seguir o modelo xxxxxxxx sem o traço')
        validacao = False 
    if not nomes_valido(nome):
        messages.error(request, 'o nome e o nome do cartão devem conter apenas letras')
        validacao = False 
    if Funcionario.objects.filter(email=email).exists():
        messages.error(request, 'o email já foi cadastrado')
        validacao = False 
    if Funcionario.objects.filter(cpf=cpf).exists():
        messages.error(request, 'o CPF já foi cadastrado')
        validacao = False 

    if Funcionario.objects.filter(rg=rg).exists():
        messages.error(request, 'o RG já foi cadastrado')
        validacao = False 

    campos = [pix, agencia,conta,banco]
    nomes = ['Pix','Agencia', 'conta', 'banco']
    iterador = -1
    for campo in campos:
        iterador = iterador+1
        if valida_campo_vazio(campo):
            messages.error(request, f'O caractere espaço não e considerado no começo do campo {nomes[iterador]}')
            validacao = False 
    return validacao
