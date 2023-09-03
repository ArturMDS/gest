from django.db import models
from pessoas.models import Pessoa


class Endereco(models.Model):
    logadouro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=80)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=80)
    pessoa = models.OneToOneField(Pessoa, related_name="endereco", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo
