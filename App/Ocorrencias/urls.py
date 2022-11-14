from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexFacilities, name="index_facilitis"),
    path('index/ocorrencia/<int:status>', views.filtro_status, name="filtro_status"),
    path('ocorrencia/<int:ocorrencia_id>', views.visualizar_ocorrencia, name="visualizar_ocorrencia"),
    path('alterar_status_ocorrencia/<int:ocorrencia_id>/<int:status>', views.alterar_status_ocorrencia, name="alterar_status_ocorrencia"),
    path('cadastrar_ocorrencia/', views.cadastrar_ocorrencia, name="cadastrar_ocorrencia"),
    path('deletar_ocorrencia/<int:ocorrencia_id>', views.deletar_ocorrencia, name="deletar_ocorrencia"),
    path('editar_ocorrencia/<int:ocorrencia_id>', views.editar_ocorrencia, name="editar_ocorrencia")
]