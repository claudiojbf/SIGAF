from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexFacilities, name="index_facilitis"),
]