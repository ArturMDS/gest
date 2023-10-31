from django.db import models
from usuarios.models import Usuario

LISTA_SITUACAO = (
    ("Pré-Cadastro", "Pendente de Homologação"),
    ("Ativo", "Ativo"),
    ("Arquivo", "Excluído do Efetivo")
)

LISTA_SANGUE = (
    ("O", "O"),
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
)

LISTA_FATORRH = (
    ("+", "Positivo"),
    ("-", "Negativo"),
)

LISTA_ESCOLARIDADE = (
    ("Analfabeto", "Analfabeto"),
    ("Fundamental Incompleto", "Fundamental Incompleto"),
    ("Fundamental Completo", "Fundamental Completo"),
    ("Médio Incompleto", "Médio Incompleto"),
    ("Médio Completo", "Médio Completo"),
    ("Superior Incompleto", "Superior Incompleto"),
    ("Superior Completo", "Superior Completo"),
    ("Pós-Graduação", "Pós-Graduação"),
    ("Mestrado", "Mestrado"),
    ("Doutorado", "Doutorado"),
)


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nasc = models.DateField()
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    nome_pai = models.CharField(max_length=250, blank=True, null=True)
    nome_mae = models.CharField(max_length=250)
    tipo_sanguineo = models.CharField(
        "Tipo Sanguíneo",
        max_length=2,
        choices=LISTA_SANGUE,
        blank=True, null=True
    )
    fator_rh = models.CharField(
        "Fator RH",
        max_length=8,
        choices=LISTA_FATORRH,
        blank=True, null=True
    )
    peso = models.IntegerField(default=70)
    altura = models.DecimalField(max_digits=3, decimal_places=2, default=1.70)
    situacao = models.CharField(
        max_length=30,
        choices=LISTA_SITUACAO,
        default="Pré-Cadastro",
    )
    escolaridade = models.CharField(
        max_length=60,
        choices=LISTA_ESCOLARIDADE,
        default="Fundamental Incompleto",
    )
    religiao = models.CharField(max_length=100, default='Não declarado')
    usuario = models.OneToOneField(Usuario, related_name="pessoas", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        permissions = (
            ('acesso', 'Usuario pode alterar'),
        )

    def __str__(self):
        return self.nome_completo


class Banco(models.Model):
    nome = models.CharField("Nome do Banco", max_length=70, null=True, blank=True)
    agencia = models.CharField("Agência", max_length=30, null=True, blank=True)
    conta = models.CharField("Conta Corrente", max_length=50, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, related_name="banco", on_delete=models.PROTECT, verbose_name="Titular")

    def __str__(self):
        return self.pessoa.nome_completo

