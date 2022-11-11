from django.db import models
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
    telefone = models.CharField(max_length=11)
    nascimento = models.DateField()
    nivel_de_usuario = models.ForeignKey(NivelDeUsuario, on_delete=models.CASCADE)
    foto_de_perfil = models.ImageField(upload_to= 'FotosPerfil', blank = True)

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = '"usuario"."usuario"'