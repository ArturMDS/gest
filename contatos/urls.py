from django.urls import path
from .views import Perfilcontato, Criarcontato

app_name = 'contatos'

urlpatterns = [
    path('cadastro/novo', Criarcontato.as_view(), name='criarcontato'),
    path('perfil/<int:pk>', Perfilcontato.as_view(), name='perfilcontato'),
]
