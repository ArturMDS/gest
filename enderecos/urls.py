from django.urls import path
from .views import Criarendereco, Perfilendereco

app_name = 'enderecos'

urlpatterns = [
    path('cadastro/novo', Criarendereco.as_view(), name='criarendereco'),
    path('perfil/<int:pk>', Perfilendereco.as_view(), name='perfilendereco'),
]
