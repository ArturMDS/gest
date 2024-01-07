from django.db import models
from quarteis.models import Quartel
from subunidades.models import Subunidade

LISTA_COMB = (
    ("Gasolina", "Gas"),
    ("Óleo Diesel", "OD"),
    ("Álcool", "Álcool"),
    ("Gasolina e Álcool", "Flex"),
)

SIT_VTR = (
    ("Disponível", "Disp"),
    ("Indisponível", "Insdisp"),
    ("Descarregado", "Descarregado"),
    ("Recolhido", "Recolhido"),
)

LISTA_ARMT = (
    ("Fuzil 7,62mm", "Fuzil 7,62mm"),
    ("Pistola 9mm", "Pistola 9mm"),
    ("Metralhadora MAG", "Metralhadora MAG"),
    ("FAP", "FAP"),
    ("FAC", "FAC"),
    ("Metralhadora .50", "Metralhadora .50"),
    ("Fuzil 5,56mm", "Fuzil 5,56mm"),
    ("Espingarda 12", "Espingarda 12"),
    ("Morteiro Pesado 120mm", "Morteiro Pesado 120mm"),
    ("Obuseiro 105mm", "Obuseiro 105mm"),
    ("Obuseiro 155mm", "Obuseiro 155mm"),
    ("Faca", "Faca"),
    ("Outros", "Outros")
)

LISTA_MUN = (
    ("Mun 7,62mm Comum", "Mun 7,62mm Comum"),
    ("Mun 9mm", "Mun 9mm"),
    ("Mun 7,62mm Tr", "Mun 7,62mm Tr"),
    ("Mun .50", "Mun .50"),
    ("Mun 5,56mm", "Mun 5,56mm"),
    ("Mun Cal 12", "Mun Cal 12"),
    ("Mun menos letal", "Mun menos letal"),
    ("Gr menos letal", "Gr menos letal"),
    ("Mun 120mm", "Mun 120mm"),
    ("Mun 105mm", "Mun 105mm"),
    ("Mun 155mm", "Mun 155mm"),
    ("Outros", "Outros")
)

LISTA_VTR = (
    ("Vtr 3/4 Ton", "Vtr 3/4 Ton"),
    ("Vtr 5 Ton", "Vtr 5 Ton"),
    ("Vtr 7 Ton", "Vtr 7 Ton"),
    ("Vtr Bld", "Vtr Bld"),
    ("Ambulância", "Ambulância"),
    ("Vtr Adm", "Vtr Adm"),
    ("Reboque Cistena", "Reboque Cistena"),
    ("Vtr Cisterna", "Vtr Cisterna"),
    ("Ônibus", "Ônibus"),
    ("Cozinha de Campanha", "Cozinha de Campanha"),
    ("Vtr Basculante", "Vtr Basculante"),
    ("Outros", "Outros")
)


class Viatura(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_VTR,
        default="Outros",
    )
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=50, blank=True, null=True)
    ano_fabricacao = models.IntegerField(default=2000)
    combustivel = models.CharField(
        max_length=25,
        choices=LISTA_COMB,
        default="Óleo Diesel",
    )
    consumo_real = models.DecimalField("Consumo Real", default=1.00, max_digits=4, decimal_places=2)
    consumo_plan = models.DecimalField("Consumo para Planejamento", default=1.00, max_digits=4, decimal_places=2)
    patrimonio = models.CharField(max_length=30, blank=True, null=True)
    troca_oleo = models.DateField(blank=True, null=True)
    fabricacao_pneu = models.DateField(blank=True, null=True)
    odometro = models.IntegerField(default=0)
    capacidade_combustivel = models.IntegerField(default=20)
    capacidade_passageiro = models.IntegerField(default=2)
    situacao = models.CharField(
        max_length=20,
        choices=SIT_VTR,
        default="Disponível",
    )
    observacoes = models.TextField(null=True, blank=True)
    unidade = models.ForeignKey(Quartel, related_name="viatura", on_delete=models.PROTECT)
    subunidade = models.ForeignKey(Subunidade, related_name="viatura", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' - ' + self.patrimonio


class Armamento(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_ARMT,
        default="Outros",
    )
    modelo = models.CharField(max_length=100, null=True, blank=True)
    calibre = models.CharField(max_length=100, null=True, blank=True)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    nr_serie = models.CharField("Número de série", max_length=50)
    qtde_tiros = models.IntegerField("Quantidade de tiros", default=0)
    situacao = models.CharField(
        max_length=20,
        choices=SIT_VTR,
        default="Disponível",
    )
    outros_nr_serie = models.CharField(max_length=50, null=True, blank=True)
    historico = models.TextField(null=True, blank=True)
    aes = models.TextField("Acessórios e Sobressalentes", null=True, blank=True)
    unidade = models.ForeignKey(Quartel, related_name="armamento", on_delete=models.PROTECT)
    subunidade = models.ForeignKey(Subunidade, related_name="armamento", on_delete=models.PROTECT)

    def __str__(self):
        return self.classificacao + ' - ' + self.modelo + ' - ' + self.nr_serie + ' - ' + self.unidade.abreviatura


class Municao(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_MUN,
        default="Outros",
    )
    tipo = models.CharField(max_length=100)
    lote = models.CharField(max_length=20)
    quantidade = models.IntegerField(default=0)
    codigo_virola = models.CharField(max_length=20)
    vencimento = models.DateField(blank=True, null=True)
    unidade = models.ForeignKey(Quartel, related_name="municao", on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo + ' - ' + self.lote + ' - ' + self.unidade.abreviatura


# TODO: data não está funcionando
class ConsumoMun(models.Model):
    atividade = models.CharField(max_length=100)
    municao = models.ForeignKey(Municao, related_name="consumo", on_delete=models.CASCADE)
    quantidade = models.IntegerField("Munição Consumida", default=0)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.atividade + ' - ' + self.municao.tipo + ' - ' + \
               self.municao.lote + ' - ' + self.municao.unidade.abreviatura


# TODO: data não está funcionando
class Alteracao(models.Model):
    disparos = models.IntegerField("Disparos efetuados", default=0)
    situacao = models.CharField(
        "Situação do Armamento",
        max_length=20,
        choices=SIT_VTR,
        default="Disponível",
    )
    data = models.DateField(auto_now=True)
    alteracao = models.TextField("Ocorrência observada", null=True, blank=True)
    armamento = models.ForeignKey(Armamento, related_name="alteracao", on_delete=models.CASCADE)

    def __str__(self):
        return self.alteracao + ' - ' + self.armamento.tipo + ' - ' + \
               self.armamento.nr_serie + ' - ' + self.armamento.unidade.abreviatura

