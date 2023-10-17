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


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nasc = models.DateField()
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    nome_pai = models.CharField(max_length=250, blank=True, null=True)
    nome_mae = models.CharField(max_length=250)
    tipo_sanguineo = models.CharField(
        max_length=2,
        choices=LISTA_SANGUE,
        blank=True, null=True
    )
    fator_rh = models.CharField(
        max_length=8,
        choices=LISTA_FATORRH,
        blank=True, null=True
    )
    peso = models.IntegerField(default=70)
    situacao = models.CharField(
        max_length=30,
        choices=LISTA_SITUACAO,
        default="Pré-Cadastro",
    )
    usuario = models.OneToOneField(Usuario, related_name="pessoas", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        permissions = (
            ('acesso', 'Usuario pode alterar'),
        )

    def __str__(self):
        return self.nome_completo
