from django.db import models

LISTA_COMB = (
    ("Gasolina", "Gas"),
    ("Óleo Diesel", "OD"),
    ("Álcool", "Álcool"),
    ("Gasolina e Álcool", "Flex"),
)

SIT_VTR = (
    ("Disponível", "Disp"),
    ("Indisponível", "Insdisp"),
    ("Descarregada", "Descarregada"),
)


class Viatura(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    ano_fabricacao = models.IntegerField(default=2000)
    combustivel = models.CharField(
        max_length=25,
        choices=LISTA_COMB,
        default="Óleo Diesel",
    )
    consumo = models.IntegerField(default=1)
    patrimonio = models.CharField(max_length=30, blank=True, null=True)
    troca_oleo = models.DateField(blank=True, null=True)
    fabricacao_pneu = models.DateField(blank=True, null=True)
    capacidade_combustivel = models.IntegerField(default=20)
    capacidade_passageiro = models.IntegerField(default=2)
    situacao = models.CharField(
        max_length=20,
        choices=SIT_VTR,
        default="Disponível",
    )

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' - ' + self.patrimonio
