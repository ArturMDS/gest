from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Usuario


class CriarUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

