from django.urls import path
from .views import Fatosobservados, Fatosobservadospessoa, \
    Criarmilitar, Criarobservacao, Perfilmilitar, Updateobservacao

app_name = 'militares'

urlpatterns = [
    path('fatosobservados/novo', Criarobservacao.as_view(), name='criarobservacao'),
    path('fatosobservados', Fatosobservados.as_view(), name='fatosobservados'),
    path('fatosobservados/<int:pk>', Fatosobservadospessoa.as_view(), name='fatosobservadospessoa'),
    path('fatosobservados/update/<int:pk>', Updateobservacao.as_view(), name='updateobservacao'),
    path('cadastro/', Criarmilitar.as_view(), name='criarmilitar'),
    path('perfil/<int:pk>', Perfilmilitar.as_view(), name='perfilmilitar'),
]
