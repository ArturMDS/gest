from django.forms import ModelForm
from .models import Viatura, Armamento, Municao
from subunidades.models import Subunidade


class ViaturaForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ViaturaForm, self).__init__(*args, **kwargs)
        unidade = user.pessoas.militar.unidade
        self.fields['subunidade'].queryset = Subunidade.objects.filter(OM=unidade)

    class Meta:
        model = Viatura
        exclude = ['unidade']


class ArmamentoForm(ModelForm):
    def __init__(self, user,  *args, **kwargs):
        super(ArmamentoForm, self).__init__(*args, **kwargs)
        unidade = user.pessoas.militar.unidade
        self.fields['subunidade'].queryset = Subunidade.objects.filter(OM=unidade)

    class Meta:
        model = Armamento
        exclude = ['unidade']


class MunicaoForm(ModelForm):
    class Meta:
        model = Municao
        exclude = ['unidade']

