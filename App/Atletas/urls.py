from django.urls import path
from . import views

urlpatterns = [
    path('atletas_index/', views.AtletaIndex, name="index_atleta"),
    path('listar_atletas/<int:modalidade_id>/', views.listar_atletas, name='listar_atletas'),
    path('cadastrar_atleta/<int:modalidade_id>/', views.cadastrar_atleta, name='cadastrar_atleta'),
    path('visualizar_atleta/<int:atleta_id>/',views.visualizar_atleta, name="visualizar_atleta")
]