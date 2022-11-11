from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_do_local")
    list_display_links = ("id", "nome_do_local")

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_da_ocorrencia", "status")
    list_display_links = ("id", "titulo_da_ocorrencia")

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)