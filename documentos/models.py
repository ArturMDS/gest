from django.db import models
from pessoas.models import Pessoa


class Documento(models.Model):
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    titulo_eleitor = models.CharField(max_length=50)
    cnh = models.CharField(max_length=20, null=True, blank=True)
    cat_cnh = models.CharField(max_length=1, null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="documento", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo
