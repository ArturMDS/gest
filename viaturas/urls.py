from django.urls import path
from .views import Viaturas, Updateviatura, Criarviatura

app_name = 'viaturas'

urlpatterns = [
    path('material/viatura', Viaturas.as_view(), name='viatura'),
    path('material/viatura/novo', Criarviatura.as_view(), name='criarviatura'),
    path('material/viatura/update/<int:pk>', Updateviatura.as_view(), name='updateviatura'),
]
