from django.urls import path
from .views import create_dados, create_armt

app_name = 'quarteis'

urlpatterns = [
    path('dados_novo/', create_dados, name='create_dados'),
    path('armt_novo/', create_armt, name='create_armt'),
]

