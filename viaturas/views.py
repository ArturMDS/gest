from django.shortcuts import reverse
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Viatura, Armamento, Municao, ConsumoMun, Alteracao
from .forms import ViaturaForm, ArmamentoForm, MunicaoForm
from quarteis.models import Quartel
from math import ceil


class Viaturas(LoginRequiredMixin, ListView):
    template_name = "viatura.html"
    model = Viatura

    def get_context_data(self, **kwargs):
        context = super(Viaturas, self).get_context_data(**kwargs)
        unidade_logada = self.request.user.pessoas.militar.unidade
        viaturas = Viatura.objects.filter(unidade=unidade_logada)
        context["viaturas"] = viaturas
        return context


class Criarviatura(LoginRequiredMixin, CreateView):
    template_name = "criarviatura.html"
    model = Viatura
    form_class = ViaturaForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoas.militar.unidade
        form.instance.unidade = unidade_logada
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(Criarviatura, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('viaturas:viatura')


class Updateviatura(LoginRequiredMixin, UpdateView):
    template_name = "updateviatura.html"
    model = Viatura
    form_class = ViaturaForm

    def get_form_kwargs(self):
        kwargs = super(Updateviatura, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('viaturas:viatura')


class Armamentos(LoginRequiredMixin, ListView):
    template_name = "armamento.html"
    model = Armamento

    def get_context_data(self, **kwargs):
        context = super(Armamentos, self).get_context_data(**kwargs)
        unidade_logada = self.request.user.pessoas.militar.unidade
        armamentos = Armamento.objects.filter(unidade=unidade_logada)
        context["armamentos"] = armamentos
        return context


class Criararmamento(LoginRequiredMixin, CreateView):
    template_name = "criararmamento.html"
    model = Armamento
    form_class = ArmamentoForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoas.militar.unidade
        form.instance.unidade = unidade_logada
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(Criararmamento, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('viaturas:armamento')


class Updatearmamento(LoginRequiredMixin, UpdateView):
    template_name = "updatearmamento.html"
    model = Armamento
    form_class = ArmamentoForm

    def get_form_kwargs(self):
        kwargs = super(Updatearmamento, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('viaturas:armamento')


class Municoes(LoginRequiredMixin, ListView):
    template_name = "municao.html"
    model = Armamento

    def get_context_data(self, **kwargs):
        context = super(Municoes, self).get_context_data(**kwargs)
        unidade_logada = self.request.user.pessoas.militar.unidade
        municoes = Municao.objects.filter(unidade=unidade_logada)
        context["municoes"] = municoes
        return context


class Criarmunicao(LoginRequiredMixin, CreateView):
    template_name = "criarmunicao.html"
    model = Municao
    form_class = MunicaoForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoas.militar.unidade
        form.instance.unidade = unidade_logada
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:municao')


class Updatemunicao(LoginRequiredMixin, UpdateView):
    template_name = "updatemunicao.html"
    model = Municao
    form_class = MunicaoForm

    def get_success_url(self):
        return reverse('viaturas:municao')


class Criarconsumo(LoginRequiredMixin, CreateView):
    template_name = "criarconsumo.html"
    model = ConsumoMun
    fields = ['atividade', 'quantidade', 'data']

    def form_valid(self, form):
        mun_id = self.request.GET['municao_id']
        municao = Municao.objects.get(id=mun_id)
        municao.quantidade -= form.instance.quantidade
        form.instance.municao = municao
        form.save()
        municao.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:municao')


class Criaralteracao(LoginRequiredMixin, CreateView):
    template_name = "criaralteracao.html"
    model = Alteracao
    fields = ['disparos', 'situacao', 'alteracao', 'data']

    def form_valid(self, form):
        armt_id = self.request.GET['armt_id']
        armamento = Armamento.objects.get(id=armt_id)
        armamento.qtde_tiros += form.instance.disparos
        form.instance.armamento = armamento
        form.save()
        armamento.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:armamento')


class DashboardArmt(LoginRequiredMixin, TemplateView):
    template_name = 'dash_armt.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardArmt, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoas.militar.unidade.id
        quartel = Quartel.objects.get(id=unidade)
        subunidades = quartel.subunidade.all()
        pst_su0 = Armamento.objects.filter(subunidade=subunidades[0], classificacao="Pistola 9mm")
        fz_su0 = Armamento.objects.filter(subunidade=subunidades[0], classificacao="Fuzil 7,62mm")
        fac_su0 = Armamento.objects.filter(subunidade=subunidades[0], classificacao="FAC")
        faca_su0 = Armamento.objects.filter(subunidade=subunidades[0], classificacao="Faca")
        epg_su0 = Armamento.objects.filter(subunidade=subunidades[0], classificacao="Espingarda 12")
        pst_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="Pistola 9mm")
        fz_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="Fuzil 7,62mm")
        fac_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="FAC")
        faca_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="Faca")
        dt_su1 = Armamento.objects.filter(subunidade=subunidades[1],
                                          modelo="DISPOSITIVO DE TREINAMENTO DE ARTILHARIA")
        pcq_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="Metralhadora .50")
        fap_su1 = Armamento.objects.filter(subunidade=subunidades[1], classificacao="FAP")
        psti_su2 = Armamento.objects.filter(subunidade=subunidades[2],
                                            classificacao="Pistola 9mm", fabricante="IMBEL")
        pstb_su2 = Armamento.objects.filter(subunidade=subunidades[2],
                                            classificacao="Pistola 9mm", fabricante="Beretta")
        fzfal_su2 = Armamento.objects.filter(subunidade=subunidades[2], modelo="FAL M964")
        fzpfal_su2 = Armamento.objects.filter(subunidade=subunidades[2], modelo="Para-FAL M964 A1 MD")
        fac_su2 = Armamento.objects.filter(subunidade=subunidades[2], classificacao="FAC")
        faca_su2 = Armamento.objects.filter(subunidade=subunidades[2], classificacao="Faca")
        epg_su2 = Armamento.objects.filter(subunidade=subunidades[2], classificacao="Espingarda 12")
        dt_su2 = Armamento.objects.filter(subunidade=subunidades[2],
                                          modelo="DISPOSITIVO DE TREINAMENTO DE ARTILHARIA")
        am_su2 = Armamento.objects.filter(subunidade=subunidades[2],
                                          modelo="LANÇADOR DE GRANADA: AM-600")
        pst_su3 = Armamento.objects.filter(subunidade=subunidades[3], classificacao="Pistola 9mm")
        fz_su3 = Armamento.objects.filter(subunidade=subunidades[3], classificacao="Fuzil 7,62mm")
        fac_su3 = Armamento.objects.filter(subunidade=subunidades[3], classificacao="FAC")
        faca_su3 = Armamento.objects.filter(subunidade=subunidades[3], classificacao="Faca")
        #numero = ceil(ri / 3)
        context["pst_su0"] = pst_su0
        context["fz_su0"] = fz_su0
        context["fac_su0"] = fac_su0
        context["faca_su0"] = faca_su0
        context["epg_su0"] = epg_su0
        context["pst_su1"] = pst_su1
        context["fz_su1"] = fz_su1
        context["fac_su1"] = fac_su1
        context["faca_su1"] = faca_su1
        context["dt_su1"] = dt_su1
        context["pcq_su1"] = pcq_su1
        context["fap_su1"] = fap_su1
        context["psti_su2"] = psti_su2
        context["pstb_su2"] = pstb_su2
        context["fzfal_su2"] = fzfal_su2
        context["fzpfal_su2"] = fzpfal_su2
        context["fac_su2"] = fac_su2
        context["faca_su2"] = faca_su2
        context["epg_su2"] = epg_su2
        context["dt_su2"] = dt_su2
        context["am_su2"] = am_su2
        context["pst_su3"] = pst_su3
        context["fz_su3"] = fz_su3
        context["fac_su3"] = fac_su3
        context["faca_su3"] = faca_su3
        return context

