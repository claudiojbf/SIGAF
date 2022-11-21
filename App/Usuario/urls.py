from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path('logout/', views.logout, name="logout"),
    path('redirecionar/', views.Redirecionar, name = "redirecionar"),
    path('cadastro_usuario/', views.cadastro_usuario, name="cadastro_usuario"),
    path('perfil/', views.perfil, name="perfil"),
    path('alterar_senha/', views.alterar_senha, name="alterar_senha"),
    path('alterar_foto_perfil', views.alterar_foto_perfil, name="alterar_foto_perfil"),
    path('alterar_dados', views.alterar_dados, name="alterar_dados")
]