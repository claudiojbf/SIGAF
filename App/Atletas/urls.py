from django.urls import path
from . import views

urlpatterns = [
    path('atletas_index/', views.AtletaIndex, name="index_atleta"),
    path('listar_atletas/<int:modalidade_id>/', views.listar_atletas, name='listar_atletas'),
    path('cadastrar_atleta/<int:modalidade_id>/', views.cadastrar_atleta, name='cadastrar_atleta'),
    path('visualizar_atleta/<int:atleta_id>/',views.visualizar_atleta, name="visualizar_atleta"),
    path('deletar_atleta/<int:atleta_id>/', views.deletar_atleta, name="deletar_atleta"),
    path('editar_atleta/<int:atleta_id>/<int:modalidade_id>', views.editar_atleta, name="editar_atleta"),
    path('alterar_foto_atleta/<int:atleta_id>', views.alterar_foto_atleta, name="alterar_foto_atleta"),
    
]