from django.db import models
from App.Usuario.models import Usuario
from datetime import datetime

# Create your models here.
class Local(models.Model):
    nome_do_local = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_do_local
    
    class Meta:
        db_table = '"facilitis"."local"'

class Ocorrencia(models.Model):
    NIVEL = (
        ("ABT", "Aberto"),
        ("EA", "Em Andamento"),
        ("C", "Concluido")
    )
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    titulo_da_ocorrencia = models.CharField(max_length=100)
    descricao_da_ocorrencia = models.TextField()
    status = models.CharField(max_length=3, choices=NIVEL, default="ABT")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_de_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo_da_ocorrencia
    class Meta:
        db_table = '"facilitis"."ocorrencia"'