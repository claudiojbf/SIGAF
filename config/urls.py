from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.Usuario.urls')),
    path('facilitis/', include('App.Ocorrencias.urls')),
    path('funcionarios/', include('App.Funcionarios.urls')),
    path('atletas/', include('App.Atletas.urls')),
    path('consultas/', include('App.Consultas.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
