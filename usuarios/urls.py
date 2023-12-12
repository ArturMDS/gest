from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from .views import Perfilusuario, Criarusuario, Perfil, ChangeDone, Novo, \
    AutoCad, AutoCadDocumento, AutoCadEndereco, AutoCadContato, AutoCadMilitar, AutoCadDone, \
    GestUsuario, ConfirmUsuario, AllUsuario, \
    UpdateAutoCadPessoa, UpdateAutoCadContato, UpdateAutoCadDocumento, UpdateAutoCadEndereco, \
    UpdateAutoCadMilitar, \
    GestFuncao

app_name = 'usuarios'

urlpatterns = [
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('autocad', Novo.as_view(), name='novo'),
    path('mudarsenha', auth_view.PasswordChangeView.as_view(success_url=reverse_lazy('usuarios:senhaalterada'),
                                                            template_name='perfilusuario.html'), name='mudarsenha'),
    path('mudarsenha/done', ChangeDone.as_view(), name='senhaalterada'),
    path('novo', Criarusuario.as_view(), name='criarusuario'),
    path('perfil/usuario/<int:pk>', Perfilusuario.as_view(), name='perfilusuario'),
    path('perfil/<int:pk>', Perfil.as_view(), name='perfil'),
    path('autocad/<int:pk>', AutoCad.as_view(), name='autocad'),
    path('autocad/contato', AutoCadContato.as_view(), name='autocadcontato'),
    path('autocad/documento', AutoCadDocumento.as_view(), name='autocaddocumento'),
    path('autocad/endereco', AutoCadEndereco.as_view(), name='autocadendereco'),
    path('autocad/militar', AutoCadMilitar.as_view(), name='autocadmilitar'),
    path('autocad/done', AutoCadDone.as_view(), name='autocaddone'),
    path('gestusuario', GestUsuario.as_view(), name='gestusuario'),
    path('confirmusuario/<int:pk>', ConfirmUsuario.as_view(), name='confirmusuario'),
    path('allusuario', AllUsuario.as_view(), name='allusuario'),
    path('autocad/update/pessoa/<int:pk>', UpdateAutoCadPessoa.as_view(), name='update_autocadpessoa'),
    path('autocad/update/contato/<int:pk>', UpdateAutoCadContato.as_view(), name='update_autocadcontato'),
    path('autocad/update/endereco/<int:pk>', UpdateAutoCadEndereco.as_view(), name='update_autocadendereco'),
    path('autocad/update/documento/<int:pk>', UpdateAutoCadDocumento.as_view(), name='update_autocaddocumento'),
    path('autocad/update/militar/<int:pk>', UpdateAutoCadMilitar.as_view(), name='update_autocadmilitar'),
    path('gestfuncao', GestFuncao.as_view(), name='gestfuncao'),
]
