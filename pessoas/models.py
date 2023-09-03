from django.db import models
from usuarios.models import Usuario

LISTA_SITUACAO = (
    ("Pré-Cadastro", "Pendente de Homologação"),
    ("Ativo", "Ativo"),
    ("Arquivo", "Excluído do Efetivo")
)


# FIXME: Estudar a possibilidade de incluir Tipo sanguíneo, fator RH, peso
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nasc = models.DateField()
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    nome_pai = models.CharField(max_length=250, blank=True, null=True)
    nome_mae = models.CharField(max_length=250)
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
