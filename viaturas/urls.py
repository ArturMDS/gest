from django.urls import path
from .views import Viaturas, Updateviatura, Criarviatura, \
    Armamentos, Criararmamento, Updatearmamento, DashboardArmt, \
    Municoes, Criarmunicao, Updatemunicao, Criarconsumo, Criaralteracao

app_name = 'viaturas'

urlpatterns = [
    path('material/viatura', Viaturas.as_view(), name='viatura'),
    path('material/viatura/novo', Criarviatura.as_view(), name='criarviatura'),
    path('material/viatura/update/<int:pk>', Updateviatura.as_view(), name='updateviatura'),
    path('material/armamento', Armamentos.as_view(), name='armamento'),
    path('material/armamento/dash', DashboardArmt.as_view(), name='dash_armt'),
    path('material/armamento/novo', Criararmamento.as_view(), name='criararmamento'),
    path('material/armamento/update/<int:pk>', Updatearmamento.as_view(), name='updatearmamento'),
    path('material/municao', Municoes.as_view(), name='municao'),
    path('material/municao/novo', Criarmunicao.as_view(), name='criarmunicao'),
    path('material/municao/update/<int:pk>', Updatemunicao.as_view(), name='updatemunicao'),
    path('material/municao/consumo', Criarconsumo.as_view(), name='criarconsumo'),
    path('material/armamento/alteracao', Criaralteracao.as_view(), name='criaralteracao'),
]
