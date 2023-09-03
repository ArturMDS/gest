from django.urls import path
from .views import Criardocumento, Perfildocumento

app_name = 'documentos'

urlpatterns = [
    path('cadastro/novo', Criardocumento.as_view(), name='criardocumento'),
    path('perfil/<int:pk>', Perfildocumento.as_view(), name='perfildocumento'),
]
