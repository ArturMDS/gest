from django.db import models
from pessoas.models import Pessoa


class Contato(models.Model):
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100, null=True, blank=True, help_text='Telefone Residencial')
    celular = models.CharField(max_length=20)
    pessoa = models.OneToOneField(Pessoa, related_name="contato", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


"""class ContatoRecado(models.Model):
    celular = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, related_name="contato_recado", on_delete=models.CASCADE)"""
