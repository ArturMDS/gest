from django.db import models
from quarteis.models import Quartel
from pessoas.models import Pessoa


class Subunidade(models.Model):
    nome = models.CharField("Nome por Extenso", max_length=70)
    OM = models.ForeignKey(Quartel, related_name="subunidade", on_delete=models.CASCADE)
    cmt = models.OneToOneField(Pessoa, related_name="su_cmt", on_delete=models.PROTECT, null=True, blank=True)
    sgte = models.OneToOneField(Pessoa, related_name="su_sgte", on_delete=models.PROTECT, null=True, blank=True)
    enc_mat = models.OneToOneField(Pessoa, related_name="su_encmat", on_delete=models.PROTECT, null=True, blank=True)
    acesso_sgte = models.ManyToManyField(Pessoa, related_name="su_acesso_sgte", blank=True)
    acesso_encmat = models.ManyToManyField(Pessoa, related_name="su_acesso_encmat", blank=True)
    abreviatura = models.CharField(max_length=40, default="Coloque a abreviatura")

    def __str__(self):
        return self.abreviatura + ' - ' + self.OM.abreviatura
