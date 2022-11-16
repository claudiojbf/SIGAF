from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('listar_funcionarios/', views.listar_funcionarios, name="listar_funcionarios"),
    path('visualizar_funcionario/<int:funcionario_id>', views.visualizar_funcionario, name="visualizar_funcionario"),
    path('deletar_funcionario/<int:funcionario_id>', views.deletar_funcionario, name="deletar_funcionario"),
    path('editar_funcionario/<int:funcionario_id>', views.editar_funcionario, name="editar_funcionario")
]