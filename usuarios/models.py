from django.db import models
from django.contrib.auth.models import AbstractUser

"""class Operacao(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    data_deslocamento = models.DateField(null=True, blank=True)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    efetivo = models.ManyToManyField("Militar", related_name="ef_total", on_delete=models.PROTECT, blank=True)"""

LISTA_ACESSO = (
    ("Estado Maior", "EM"),
    ("Comandante", "Cmt SU"),
    ("Sargenteante", "Sgte SU"),
    ("básico", "Acesso básico"),
    ("novo", "Novo usuário"),
)


class Usuario(AbstractUser):
    email = models.EmailField(max_length=100)
    acesso = models.CharField(
        max_length=30,
        choices=LISTA_ACESSO,
        default="novo",
    )
    numero = models.IntegerField(default=0)
