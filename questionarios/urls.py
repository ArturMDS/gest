from django.urls import path
from .views import Createquestionarioum, Createquestionariodois, Createquestionariotres

app_name = 'questionarios'

urlpatterns = [
    path('create/questionario1', Createquestionarioum.as_view(), name='create_questionario_um'),
    path('create/questionario2', Createquestionariodois.as_view(), name='create_questionario_dois'),
    path('create/questionario3', Createquestionariotres.as_view(), name='create_questionario_tres')
]
