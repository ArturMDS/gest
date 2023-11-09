from django.db import models
from pessoas.models import Pessoa


class Questionarioum(models.Model):
    pergunta_um = models.CharField(max_length=50)
    pergunta_dois = models.CharField(max_length=50)
    pergunta_tres = models.CharField(max_length=50)
    pergunta_quatro = models.CharField(max_length=50)
    pergunta_cinco = models.CharField(max_length=3)
    pergunta_seis = models.CharField(max_length=50)
    pergunta_sete = models.CharField(max_length=3)
    pergunta_oito = models.CharField(max_length=100, null=True, blank=True)
    pergunta_nove = models.CharField(max_length=100, null=True, blank=True)
    pergunta_dez = models.CharField(max_length=200, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, related_name="questionario_um", on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome_completo


class Questionariodois(models.Model):
    pergunta_um = models.CharField(max_length=3)
    pergunta_dois = models.CharField(max_length=3)
    pergunta_tres = models.CharField(max_length=50)
    pergunta_quatro = models.CharField(max_length=50)
    pergunta_cinco = models.CharField(max_length=3)
    pergunta_seis = models.CharField(max_length=200)
    pergunta_sete = models.CharField(max_length=50)
    pergunta_oito = models.CharField(max_length=3)
    pergunta_nove = models.CharField(max_length=200)
    pergunta_dez = models.CharField(max_length=3)
    pergunta_onze = models.CharField(max_length=50)
    pergunta_doze = models.CharField(max_length=3)
    pergunta_treze = models.CharField(max_length=3)
    pergunta_quatorze = models.CharField(max_length=3)
    pergunta_quinze = models.CharField(max_length=3)
    pergunta_dezesseis = models.CharField(max_length=3)
    pergunta_dezessete = models.CharField(max_length=3)
    pergunta_dezoito = models.CharField(max_length=3)
    pergunta_dezenove = models.CharField(max_length=50)
    pergunta_vinte = models.CharField(max_length=3)
    pergunta_vinteum = models.CharField(max_length=3)
    pergunta_vintedois = models.CharField(max_length=3)
    pergunta_vintetres = models.CharField(max_length=50)
    pergunta_vintequatro = models.CharField(max_length=3)
    pergunta_vintecinco = models.CharField(max_length=3)
    pergunta_vinteseis = models.CharField(max_length=3)
    pergunta_vintesete = models.CharField(max_length=3)
    pessoa = models.ForeignKey(Pessoa, related_name="questionario_dois", on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome_completo


class Questionariotres(models.Model):
    pergunta_um = models.CharField(max_length=3)
    pergunta_dois = models.CharField(max_length=3)
    pergunta_tres = models.CharField(max_length=300)
    pergunta_quatro = models.CharField(max_length=3)
    pergunta_cinco = models.CharField(max_length=3)
    pergunta_seis = models.CharField(max_length=300)
    pessoa = models.ForeignKey(Pessoa, related_name="questionario_tres", on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome_completo
