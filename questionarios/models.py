from django.db import models
from pessoas.models import Pessoa


class Questao(models.Model):
    pergunta = models.CharField(max_length=200)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.pergunta


class Gabarito(models.Model):
    resposta = models.CharField(max_length=100)
    questao = models.ForeignKey(Questao, related_name="gabarito", on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, related_name="resposta", on_delete=models.PROTECT)
