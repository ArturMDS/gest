from django.urls import path
from .views import create_dados

app_name = 'quarteis'

urlpatterns = [
    path('dados_novo/', create_dados, name='create_dados')
]

