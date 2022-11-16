from django.urls import path
from . import views

urlpatterns = [
    path('atletas_index/', views.AtletaIndex, name="index_atleta"),
    path('visualizar_atletas/<int:modalidade_id>/', views.visualizar_atletas, name='visualizar_atletas'),
    path('cadastrar_atleta/<int:modalidade_id>/', views.cadastrar_atleta, name='cadastrar_atleta')
]