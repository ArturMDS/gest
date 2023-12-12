from django.db import models
from pessoas.models import Pessoa


class Quartel(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome por Extenso')
    abreviatura = models.CharField(max_length=40)
    esc_sup = models.CharField(max_length=70, help_text='Nome por Extenso', null=True, blank=True)
    abrv_esc_sup = models.CharField(max_length=40, help_text='Abreviatura do Esc Sup', null=True, blank=True)
    divisao = models.CharField(max_length=70, help_text='Nome por Extenso', null=True, blank=True)
    abrv_divisao = models.CharField(max_length=40, help_text='Abreviatura da Divisão de Exército', null=True, blank=True)
    cmdo_mil_a = models.CharField(max_length=70, help_text='Nome por Extenso', null=True, blank=True)
    abrv_cma = models.CharField(max_length=40, help_text='Abreviatura do Cmdo Mil A', null=True, blank=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    nome_historico = models.CharField(max_length=70, help_text='Nome por Extenso', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)
    dados = models.FileField(upload_to="uploads/", null=True, blank=True)
    cmt = models.OneToOneField(Pessoa, related_name="quartel_cmt", on_delete=models.PROTECT, null=True, blank=True)
    s1 = models.OneToOneField(Pessoa, related_name="quartel_s1", on_delete=models.PROTECT, null=True, blank=True)
    s2 = models.OneToOneField(Pessoa, related_name="quartel_s2", on_delete=models.PROTECT, null=True, blank=True)
    s3 = models.OneToOneField(Pessoa, related_name="quartel_s3", on_delete=models.PROTECT, null=True, blank=True)
    s4 = models.OneToOneField(Pessoa, related_name="quartel_s4", on_delete=models.PROTECT, null=True, blank=True)
    acesso_s1 = models.ManyToManyField(Pessoa, related_name="acesso_s1", blank=True)
    acesso_s2 = models.ManyToManyField(Pessoa, related_name="acesso_s2", blank=True)
    acesso_s3 = models.ManyToManyField(Pessoa, related_name="acesso_s3", blank=True)
    acesso_s4 = models.ManyToManyField(Pessoa, related_name="acesso_s4", blank=True)
    oficiais = models.ManyToManyField(Pessoa, related_name="oficiais", blank=True)
    quadros = models.ManyToManyField(Pessoa, related_name="quadros", blank=True)

    def __str__(self):
        return self.abreviatura
