from django.db import models
from pessoas.models import Pessoa


class Documento(models.Model):
    rg = models.CharField("RG", max_length=15)
    cpf = models.CharField("CPF", max_length=15)
    titulo_eleitor = models.CharField(max_length=50)
    zona_eleitoral = models.CharField(max_length=10, default=0000)
    secao_eleitoral = models.CharField(max_length=10, default=0000)
    cnh = models.CharField(max_length=20, null=True, blank=True)
    cat_cnh = models.CharField("Categoria da CNH", max_length=2, null=True, blank=True)
    data_primeira_habilitacao = models.DateField("Primeira Habilitação", null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="documento", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo
