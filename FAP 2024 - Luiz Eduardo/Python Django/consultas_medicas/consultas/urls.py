from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar_paciente/', views.cadastro_paciente, name='cadastro_paciente'),
]
