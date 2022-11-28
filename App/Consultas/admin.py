from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'criacao')
    list_display_links = ('id',)

@admin.register(EstruturaLesionada)
class EstruturaLesionadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estrutura_lesionada')
    list_display_links = ('id',)

@admin.register(RegiaoDoCorpo)
class RegiaoDoCorpoAdmin(admin.ModelAdmin):
    list_display = ('id', 'parte_do_corpo')
    list_display_links = ('id',)

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'criacao')
    list_display_links = ('id',)

@admin.register(ExamesComplementares)
class ExamesComplementaresAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_de_exame')
    list_display_links = ('id',)