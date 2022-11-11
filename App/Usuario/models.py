from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class NivelDeUsuario(models.Model):
    sigla = models.CharField(max_length = 3)
    descricao_do_nivel = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao_do_nivel
    
    class Meta:
        db_table = '"usuario"."nivel_de_usuario"'

class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, blank=True)
    nascimento = models.DateField()
    nivel_de_usuario = models.ForeignKey(NivelDeUsuario, on_delete=models.CASCADE)
    foto_de_perfil = models.ImageField(upload_to= 'FotosPerfil', blank = True)
    data_de_registro = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        db_table = '"usuario"."usuario"'