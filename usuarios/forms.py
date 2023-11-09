from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Usuario
from militares.models import Militar


class CriarUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']


class CriarAutoCadMilitarForm(forms.ModelForm):
    nome_guerra = forms.CharField(
        label="Nome de guerra é como o militar "
              "será conhecido no quartel\n"
              "caso seja selecionado, como o senhor gostaria "
              "de ser chamado (escolha 1 ou 2 de seu próprio nome completo)"
    )

    class Meta:
        model = Militar
        fields = ['nome_guerra', 'unidade']

