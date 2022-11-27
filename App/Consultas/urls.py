from django.urls import path
from . import views

urlpatterns = [
    path('index_consultas/', views.index_consultas, name="index_consultas"),
    path('visualizar_atleta/<int:atleta_id>', views.visualizar_atleta_consulta, name="visualizar_atleta_consulta"),
    path('listar_consultas/<int:atleta_id>', views.listar_consultas, name="listar_consultas"),
    path('criar_consulta/<int:atleta_id>', views.criar_consulta, name="criar_consulta"),
    path('consulta_geral/<int:consulta_id>',views.consulta_geral, name="consulta_geral" )
]