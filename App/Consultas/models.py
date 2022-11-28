from django.db import models
from App.Atletas.models import Atleta
from datetime import datetime

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Consulta(Base):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

    def __str__(self):
        return self.atleta.nome + " - " +  self.criacao.strftime('%d-%m-%Y %H:%M')
    class Meta:
        db_table = '"consultas"."consulta"'

class EstruturaLesionada(models.Model):
    estrutura_lesionada = models.CharField(max_length=100)

    def __str__(self):
        return self.estrutura_lesionada
    class Meta:
        db_table = '"consultas"."estruturalesionada"'

class RegiaoDoCorpo(models.Model):
    parte_do_corpo = models.CharField(max_length=100)

    def __str__(self):
        return self.parte_do_corpo

    class Meta:
        db_table = '"consultas"."regiodocorpo"'

class Entrada(Base):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    estrutura_lesionada = models.ForeignKey(EstruturaLesionada, on_delete=models.CASCADE)
    regiao_corpo = models.ForeignKey(RegiaoDoCorpo, on_delete=models.CASCADE)
    observacao = models.TextField()

    def __str__(self):
        return self.criacao.strftime('%d-%m-%Y %H:%M')

    class Meta:
        db_table = '"consultas"."entrada"'
    
class ExamesComplementares(models.Model):
    tipo_de_exame = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_de_exame

    class Meta:
        db_table = '"consultas"."examecomplementares"'

class Tratamento(Base):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    justificativa = models.TextField()
    

    def __str__(self):
        return self.criacao.strftime('%d-%m-%Y %H:%M')

    class Meta:
        db_table = '"consultas"."tratamento"'

class ExameTratamento(Base):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    exame_complementar = models.ForeignKey(ExamesComplementares, on_delete=models.CASCADE)
    imagem_exame = models.ImageField(upload_to = 'FotoExames',blank=True, null=True)
    justificativa_complementares = models.TextField()

    def __str__(self):
        return self.criacao.strftime('%d-%m-%Y %H:%M')

    class Meta:
        db_table = '"consultas"."exametratamento"'

class Saida(Base):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    justificativa = models.TextField()

    def __str__(self):
        return self.criacao.strftime('%d-%m-%Y %H:%M')

    class Meta:
        db_table = '"consultas"."saida"'

class Manutencao(Base):
    TIPO = (
        ("R", "Recovery"),
        ("A", "Analgesia"),
        ("O", "Terapia Manual Osteopatia"),
        ("M", "Terapia Manual Manipulação"),
    )
    tipo_manutencao = models.CharField(max_length=1, choices=TIPO)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    justificativa = models.TextField()

    def __str__(self):
        return self.criacao.strftime('%d-%m-%Y %H:%M')

    class Meta:
        db_table = '"consultas"."manutencao"'

