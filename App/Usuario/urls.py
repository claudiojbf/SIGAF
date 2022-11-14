from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path('logout/', views.logout, name="logout"),
    path('redirecionar/', views.Redirecionar, name = "redirecionar"),
    path('cadastro_usuario/', views.cadastro_usuario, name="cadastro_usuario"),
]