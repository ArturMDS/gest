from django.db import models
from django.utils import timezone
from pessoas.models import Pessoa
from subunidades.models import Subunidade
from quarteis.models import Quartel

LISTA_PG = (
    ("General de Exército", "Gen Ex"),
    ("General de Divisão", "Gen Div"),
    ("General de Brigada", "Gen Bda"),
    ("Coronel", "Cel"),
    ("Tenente Coronel", "Ten Cel"),
    ("Major", "Maj"),
    ("Capitão", "Cap"),
    ("1º Tenente", "1º Ten"),
    ("2º Tenente", "2º Ten"),
    ("Aspirante à Oficial", "Asp Of"),
    ("Subtenente", "ST"),
    ("1º Sargento", "1º Sgt"),
    ("2º Sargento", "2º Sgt"),
    ("3º Sargento", "3º Sgt"),
    ("Cabo", "Cabo"),
    ("Solcado NB", "Sd NB"),
    ("Soldado EV", "Sd EV")
)

LISTA_TIPO = (
    ("positiva", "FO+"),
    ("negativa", "FO-"),
    ("neutra", "N")
)

LISTA_PUN = (
    ("Justificado", "Justificado"),
    ("Advertência de Caráter Reservado", "ACR"),
    ("Advertência de Caráter Ostensivo", "ACO"),
    ("Impedimento Disciplinar", "ID"),
    ("Repreensão", "Rep"),
    ("Detenção", "Det"),
    ("Prisão", "Prisão"),
)


class Qualificacao(models.Model):
    qm = models.CharField(max_length=80)

    def __str__(self):
        return self.qm


class Militar(models.Model):
    nome_guerra = models.CharField(max_length=80)
    identidade = models.CharField(max_length=15, null=True, blank=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    subunidade = models.ForeignKey(Subunidade, related_name="mil_su", on_delete=models.PROTECT)
    unidade = models.ForeignKey(Quartel, related_name="mil_om", on_delete=models.PROTECT)
    qualificacao = models.ForeignKey('Qualificacao', related_name="mil_qualif", on_delete=models.PROTECT, null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="militar", on_delete=models.CASCADE)
    posto_grad = models.CharField(
        max_length=30,
        choices=LISTA_PG,
        default="Soldado EV",
    )

    def __str__(self):
        return self.nome_guerra


class Atributos(models.Model):
    camaradagem = models.IntegerField(default=100)
    iniciativa = models.IntegerField(default=100)
    persistencia = models.IntegerField(default=100)
    responsabilidade = models.IntegerField(default=100)
    coragem = models.IntegerField(default=100)
    disciplina = models.IntegerField(default=100)
    apresentacao = models.IntegerField(default=100)
    dedicacao = models.IntegerField(default=100)
    resistencia_fisica = models.IntegerField(default=100)
    conhecimento_tecnico = models.IntegerField(default=100)
    militar = models.OneToOneField(Militar, related_name="atributos", on_delete=models.CASCADE)

    def __str__(self):
        return self.militar.nome_guerra


class Observacao(models.Model):
    tipo = models.CharField(
        max_length=10,
        choices=LISTA_TIPO,
        default="neutra",
    )
    relato_fato = models.TextField(max_length=500)
    arrolado = models.ForeignKey('Militar', related_name="mil_arrolado", on_delete=models.PROTECT)
    participante = models.ForeignKey('Militar', related_name="mil_part", on_delete=models.PROTECT)
    data = models.DateField(default=timezone.now)
    nr_processo = models.IntegerField(default=0)
    solucao = models.CharField(
        max_length=50,
        choices=LISTA_PUN,
        default="Justificado",
    )
    dias = models.IntegerField(blank=True, null=True)
    publicacao_bi = models.CharField(max_length=200, blank=True, null=True)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.arrolado.nome_guerra
