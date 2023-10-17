from django.urls import path
from .views import Fatosobservados, Fatosobservadospessoa, \
    Criarmilitar, Criarobservacao, Perfilmilitar, \
    Updateobservacao, Criardestino, Verdestino, Updatedestino, \
    Fatd, Fdi

app_name = 'militares'

urlpatterns = [
    path('fatosobservados/novo', Criarobservacao.as_view(), name='criarobservacao'),
    path('fatosobservados', Fatosobservados.as_view(), name='fatosobservados'),
    path('fatosobservados/<int:pk>', Fatosobservadospessoa.as_view(), name='fatosobservadospessoa'),
    path('fatosobservados/update/<int:pk>', Updateobservacao.as_view(), name='updateobservacao'),
    path('cadastro/', Criarmilitar.as_view(), name='criarmilitar'),
    path('perfil/<int:pk>', Perfilmilitar.as_view(), name='perfilmilitar'),
    path('fatosobservados/fatd/<int:pk>', Fatd.as_view(), name='fatd'),
    # TODO: terminar a fdi para finalizar essa funcionalidade
    path('fatosobservados/fdi/<int:pk>', Fdi.as_view(), name='fdi'),
    # TODO: testar
    path('destino', Verdestino.as_view(), name='destino'),
    path('destino/update/<int:pk>', Updatedestino.as_view(), name='updatedestino'),
    path('destino/novo', Criardestino.as_view(), name='criardestino'),
]
