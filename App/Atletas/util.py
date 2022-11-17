from validate_docbr import CPF

def validar_documentos(cpf):
    cpf_i = CPF()
    return cpf_i.validate(cpf)