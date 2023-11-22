from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Viatura, Armamento, Municao
from .forms import ViaturaForm, ArmamentoForm, MunicaoForm


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

