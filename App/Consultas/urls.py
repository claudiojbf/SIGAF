from django.urls import path
from . import views

urlpatterns = [
    path('index_consultas/', views.index_consultas, name="index_consultas"),
    path('visualizar_atleta/<int:atleta_id>', views.visualizar_atleta_consulta, name="visualizar_atleta_consulta"),
    path('listar_consultas/<int:atleta_id>', views.listar_consultas, name="listar_consultas"),
    path('criar_consulta/<int:atleta_id>', views.criar_consulta, name="criar_consulta"),
    path('consulta_geral/<int:consulta_id>',views.consulta_geral, name="consulta_geral" ),
    path('criar_entrada/<int:consulta_id>', views.criar_entrada, name="criar_entrada"),
    path('criar_tratamento/<int:consulta_id>', views.criar_tratamento, name="criar_tratamento"),
    path('criar_exame_complementar/<int:consulta_id>', views.criar_exame_complementar, name="criar_exame_complementar"),
    path('criar_saida/<int:consulta_id>', views.criar_saida, name="criar_saida"),
    path('criar_manutencao/<int:consulta_id>', views.criar_manutencao, name="criar_manutencao"),
    path('visualizar_imagem/<int:consulta_id>', views.visualizar_imagem, name="visualizar_imagem_consulta"),
    path('retornar_consulta/<int:consulta_id>', views.retornar_consulta, name="retornar_consulta")
]