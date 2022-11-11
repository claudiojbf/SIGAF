from django.contrib import admin
from .models import NivelDeUsuario, Usuario
# Register your models here.

@admin.register(NivelDeUsuario)
class NivelDeUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao_do_nivel', 'sigla')
    list_display_links = ('id', 'descricao_do_nivel')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    list_display_link = ('id', 'usuario')