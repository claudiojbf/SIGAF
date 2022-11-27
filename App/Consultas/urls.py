from django.urls import path
from . import views

urlpatterns = [
    path('index_consultas/', views.index_consultas, name="index_consultas"),
    path('visualizar_atleta/<int:atleta_id>', views.visualizar_atleta_consulta, name="visualizar_atleta_consulta")
]