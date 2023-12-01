from django.urls import path
from .views import Cadastro, \
    Cadastropessoa, \
    Criarpessoa, \
    Delete, \
    Perfilpessoa, \
    ListConscrito, \
    ReadConscrito, \
    Formulario, \
    Pesquisacadastro

app_name = 'pessoas'

urlpatterns = [
    path('cadastro', Cadastro.as_view(), name='cadastro'),
    path('cadastro/pesquisa', Pesquisacadastro.as_view(), name='pesquisacadastro'),
    path('cadastro/<int:pk>', Cadastropessoa.as_view(), name='cadastropessoa'),
    path('cadastro/novo', Criarpessoa.as_view(), name='criarpessoa'),
    path('cadastro/delete/<int:pk>', Delete.as_view(), name='delete'),
    path('perfil/<int:pk>', Perfilpessoa.as_view(), name='perfilpessoa'),
    path('cadastro/listconscrito', ListConscrito.as_view(), name='listconscrito'),
    path('cadastro/readconscrito/<int:pk>', ReadConscrito.as_view(), name='readconscrito'),
    path('cadastro/formulario/<int:pk>', Formulario.as_view(), name='formulario'),
]
