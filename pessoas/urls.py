from django.urls import path
from .views import Cadastro, Cadastropessoa, Criarpessoa, Delete, Perfilpessoa

app_name = 'pessoas'

urlpatterns = [
    path('cadastro', Cadastro.as_view(), name='cadastro'),
    path('cadastro/<int:pk>', Cadastropessoa.as_view(), name='cadastropessoa'),
    path('cadastro/novo', Criarpessoa.as_view(), name='criarpessoa'),
    path('cadastro/delete/<int:pk>', Delete.as_view(), name='delete'),
    path('perfil/<int:pk>', Perfilpessoa.as_view(), name='perfilpessoa'),
]
