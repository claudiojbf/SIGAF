from django.db import models
from datetime import date

# Create your models here

class Modalidade(models.Model):
    nome_da_modalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_da_modalidade
    
    class Meta:
        db_table = '"atletas"."modalidade"'

class SubDivisao(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    sub_divisao = models.CharField(max_length=10)

    def __str__(self):
        if len(self.sub_divisao) <= 2:
            return "Sub: " + self.sub_divisao
        return self.sub_divisao
    
    class Meta:
        db_table = '"atletas"."subdivisao"'

class Posicao(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    posicao = models.CharField(max_length=50)

    def __str__(self):
        return self.posicao

    class Meta:
        db_table = '"atletas"."posicao"'

class Atleta(models.Model):
    PERNA = (
        ("D", "Diretita"),
        ("E", "Esquerda"),
        ("A", "Ambidestro")
    )
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    posicao = models.ForeignKey(Posicao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    perna_dominante = models.CharField(max_length=1, choices=PERNA)
    matricula_escolar = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    nivel_escolar = models.CharField(max_length=50, blank=True, null=True)
    naturalidade_uf= models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    numero_da_casa = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    whatsapp2 = models.CharField(max_length=11, blank=True, null=True)
    nome_pai = models.CharField(max_length=50, blank=True, null=True)
    nome_mae = models.CharField(max_length=50, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=50, blank=True, null=True)
    telefone_responsavel2 = models.CharField(max_length=50, blank=True, null=True)
    altura = models.CharField(max_length=5)
    peso = models.CharField(max_length=7)
    plano_saude = models.CharField(max_length=100, blank=True, null=True)
    alergia = models.CharField(max_length=100, default="Nenhuma", null=True)
    foto_atleta = models.ImageField(upload_to='FotoAtleta', blank=True)

    def __str__(self):
        return self.nome

    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    class Meta:
        db_table = '"atletas"."atleta"'