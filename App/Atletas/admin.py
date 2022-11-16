from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_da_modalidade")
    list_display_links = ("id", "nome_da_modalidade")

@admin.register(Posicao)
class PosicaoAdmin(admin.ModelAdmin):
    list_display = ("id", "posicao", "modalidade")
    list_display_links = ("id", "posicao")

@admin.register(SubDivisao)
class SubDivisaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_divisao', 'modalidade')
    list_display_links = ('id', 'sub_divisao')

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')