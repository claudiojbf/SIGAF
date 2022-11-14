from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_funcionario', views.cadastro_funcionario, name='cadastro_funcionario'),
]