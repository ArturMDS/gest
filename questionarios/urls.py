from django.urls import path
from .views import Createquestionarioum, \
    Createquestionariodois, \
    Createquestionariotres, \
    Updatequestionarioum, \
    Updatequestionariodois, \
    Updatequestionariotres, \
    Updateum, \
    Updatedois, \
    Updatetres

app_name = 'questionarios'

urlpatterns = [
    path('create/questionario1', Createquestionarioum.as_view(), name='create_questionario_um'),
    path('create/questionario2', Createquestionariodois.as_view(), name='create_questionario_dois'),
    path('create/questionario3', Createquestionariotres.as_view(), name='create_questionario_tres'),
    path('update/questionario1/<int:pk>', Updatequestionarioum.as_view(), name='update_questionario_um'),
    path('update/questionario2/<int:pk>', Updatequestionariodois.as_view(), name='update_questionario_dois'),
    path('update/questionario3/<int:pk>', Updatequestionariotres.as_view(), name='update_questionario_tres'),
    path('update/um/<int:pk>', Updateum.as_view(), name='update_um'),
    path('update/dois/<int:pk>', Updatedois.as_view(), name='update_dois'),
    path('update/tres/<int:pk>', Updatetres.as_view(), name='update_tres')
]
