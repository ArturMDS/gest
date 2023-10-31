from django.db import models
from quarteis.models import Quartel


class Subunidade(models.Model):
    nome = models.CharField("Nome por Extenso", max_length=70)
    OM = models.ForeignKey(Quartel, related_name="subunidade", on_delete=models.CASCADE)
    cmt = models.CharField("Nome completo do Comandante", max_length=250, null=True, blank=True)
    abreviatura = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.abreviatura + ' - ' + self.OM.abreviatura
