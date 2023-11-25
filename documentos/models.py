from django.db import models
from pessoas.models import Pessoa


class Documento(models.Model):
    rg = models.CharField("RG", max_length=25)
    cpf = models.CharField("CPF", max_length=25)
    titulo_eleitor = models.CharField(max_length=50, null=True, blank=True)
    zona_eleitoral = models.CharField(max_length=20, default=0000, null=True, blank=True)
    secao_eleitoral = models.CharField(max_length=20, default=0000, null=True, blank=True)
    cnh = models.CharField(max_length=30, null=True, blank=True)
    cat_cnh = models.CharField("Categoria da CNH", max_length=10, null=True, blank=True)
    data_primeira_habilitacao = models.DateField("Primeira Habilitação", null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="documento", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo
