from django.db import models
from quarteis.models import Quartel


class Subunidade(models.Model):
    nome = models.CharField(max_length=70)
    OM = models.ForeignKey(Quartel, related_name="subunidade", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' - ' + self.OM.abreviatura
