from django.db import models


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
    cmt = models.CharField("Nome completo do Comandante", max_length=250, null=True, blank=True)

    def __str__(self):
        return self.abreviatura
