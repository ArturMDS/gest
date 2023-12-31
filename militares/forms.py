from django.forms import ModelForm
from .models import Militar, Observacao, Destino
from subunidades.models import Subunidade


class CriarMilitarForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CriarMilitarForm, self).__init__(*args, **kwargs)
        self.fields['subunidade'].queryset = Subunidade.objects.filter(OM=user.pessoas.militar.unidade)

    class Meta:
        model = Militar
        fields = ['nome_guerra', 'identidade', 'numero', 'subunidade', 'qualificacao', 'posto_grad', 'data_praca']


class UpdateObservacaoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(UpdateObservacaoForm, self).__init__(*args, **kwargs)
        self.fields['arrolado'].queryset = Militar.objects.filter(unidade=user.pessoas.militar.unidade)

    class Meta:
        model = Observacao
        fields = ['tipo', 'relato_fato', 'arrolado', 'solucao', 'dias', 'enquadramento', 'publicacao_bi']


class PerfilMilitarForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PerfilMilitarForm, self).__init__(*args, **kwargs)
        self.fields['subunidade'].queryset = Subunidade.objects.filter(OM=user.pessoas.militar.unidade)

    class Meta:
        model = Militar
        fields = ['nome_guerra', 'identidade', 'numero', 'subunidade', 'qualificacao', 'posto_grad', 'data_praca']


class CriarDestinoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        pessoa = user.pessoas
        s1 = user.pessoas.militar.unidade.s1
        aux_s1 = user.pessoas.militar.unidade.acesso_s1.all()
        cmt_su = user.pessoas.militar.subunidade.cmt
        quadros_su = user.pessoas.militar.subunidade.quadros.all()
        if (pessoa == s1) or (pessoa in aux_s1):
            super(CriarDestinoForm, self).__init__(*args, **kwargs)
            self.fields['militar'].queryset = Militar.objects.filter(unidade=user.pessoas.militar.unidade)
        elif (pessoa == cmt_su) or (pessoa in quadros_su):
            super(CriarDestinoForm, self).__init__(*args, **kwargs)
            self.fields['militar'].queryset = Militar.objects.filter(subunidade=user.pessoas.militar.subunidade)

    class Meta:
        model = Destino
        fields = ['check_in', 'check_out', 'motivo', 'militar']


class UpdateDestinoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(UpdateDestinoForm, self).__init__(*args, **kwargs)
        self.fields['militar'].queryset = Militar.objects.filter(subunidade=user.pessoas.militar.subunidade)

    class Meta:
        model = Destino
        fields = ['check_in', 'check_out', 'motivo', 'militar']

