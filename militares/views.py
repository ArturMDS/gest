from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Observacao, Militar, Qualificacao
from pessoas.models import Pessoa


class Fatosobservados(LoginRequiredMixin, ListView):
    template_name = "fatosobservados.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(Fatosobservados, self).get_context_data(**kwargs)
        if self.request.user.acesso == 'Estado Maior':
            om_logada = self.request.user.pessoas.militar.subunidade.OM
            militares = Militar.objects.filter(unidade=om_logada).order_by("-posto_grad")
            context["militares"] = militares
            return context
        else:
            su_logada = self.request.user.pessoas.militar.subunidade
            militares = Militar.objects.filter(subunidade=su_logada).order_by("-posto_grad")
            context["militares"] = militares
            return context


# FIXME: Botão FATD não está funcionando
class Fatosobservadospessoa(LoginRequiredMixin, DetailView):
    template_name = "fatosobservadospessoa.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(Fatosobservadospessoa, self).get_context_data(**kwargs)
        observacoes = Observacao.objects.all()
        context["observacoes"] = observacoes
        return context


class Criarmilitar(LoginRequiredMixin, CreateView):
    template_name = "criarmilitar.html"
    model = Militar
    fields = ['nome_guerra', 'identidade', 'numero', 'subunidade', 'qualificacao', 'posto_grad']

    def get_context_data(self, **kwargs):
        context = super(Criarmilitar, self).get_context_data(**kwargs)
        data = {'id': self.request.GET['novo_id']}
        pessoa = Pessoa.objects.get(id=data['id'])
        context["pessoa"] = pessoa
        return context

    def form_valid(self, form):
        data = {'id': self.request.GET['novo_id']}
        form.instance.pessoa = Pessoa.objects.get(id=data['id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        data = {'id': self.request.GET['novo_id']}
        pessoa = Pessoa.objects.get(id=data['id'])
        return reverse('pessoas:cadastropessoa', kwargs={"pk": pessoa.id})


class Criarobservacao(LoginRequiredMixin, CreateView):
    template_name = "criarobservacao.html"
    model = Observacao
    fields = ['tipo', 'relato_fato', 'arrolado']

    def form_valid(self, form):
        militar = Militar.objects.get(id=self.request.user.pessoas.militar.id)
        form.instance.participante = militar
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        observacao = Observacao.objects.all().last()
        observacao.nr_processo = int(observacao.id) + 1
        observacao.save()
        return reverse('militares:fatosobservados')


class Updateobservacao(LoginRequiredMixin, UpdateView):
    template_name = "updateobservacao.html"
    model = Observacao
    fields = ['tipo', 'relato_fato', 'arrolado', 'solucao', 'dias', 'publicacao_bi']

    def form_valid(self, form):
        if form.instance.tipo == 'negativa' and form.instance.solucao == 'Advertência de Caráter Reservado':
            form.instance.pontos = int(-2)
        elif form.instance.tipo == 'negativa' and form.instance.solucao == 'Advertência de Caráter Ostensivo':
            form.instance.pontos = int(-3)
        elif form.instance.tipo == 'negativa' and form.instance.solucao == 'Impedimento Disciplinar':
            form.instance.pontos = int(-4)
        elif form.instance.tipo == 'negativa' and form.instance.solucao == 'Repreensão':
            form.instance.pontos = int(-5)
        elif form.instance.tipo == 'negativa' and form.instance.solucao == 'Detenção':
            form.instance.pontos = int(-6)
        elif form.instance.tipo == 'negativa' and form.instance.solucao == 'Prisão':
            form.instance.pontos = int(-7)
        elif form.instance.tipo == 'positiva':
            form.instance.pontos = 4
        elif form.instance.tipo == 'neutra':
            form.instance.pontos = 4
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        observacao = Observacao.objects.get(id=self.get_object().id)
        if 'camaradagem' in self.request.POST:
            observacao.arrolado.atributos.camaradagem += observacao.pontos
        if 'iniciativa' in self.request.POST:
            observacao.arrolado.atributos.iniciativa += observacao.pontos
        if 'persistencia' in self.request.POST:
            observacao.arrolado.atributos.persistencia += observacao.pontos
        if 'responsabilidade' in self.request.POST:
            observacao.arrolado.atributos.responsabilidade += observacao.pontos
        if 'coragem' in self.request.POST:
            observacao.arrolado.atributos.coragem += observacao.pontos
        if 'disciplina' in self.request.POST:
            observacao.arrolado.atributos.disciplina += observacao.pontos
        if 'apresentacao' in self.request.POST:
            observacao.arrolado.atributos.apresentacao += observacao.pontos
        if 'dedicacao' in self.request.POST:
            observacao.arrolado.atributos.dedicacao += observacao.pontos
        if 'resistencia_fisica' in self.request.POST:
            observacao.arrolado.atributos.resistencia_fisica += observacao.pontos
        if 'conhecimento_tecnico' in self.request.POST:
            observacao.arrolado.atributos.conhecimento_tecnico += observacao.pontos
        observacao.arrolado.atributos.save()
        return reverse('militares:fatosobservadospessoa', kwargs={"pk": observacao.arrolado.pessoa.id})


class Perfilmilitar(LoginRequiredMixin, UpdateView):
    template_name = "perfilmilitar.html"
    model = Militar
    fields = ['nome_guerra', 'identidade', 'numero',
              'subunidade', 'qualificacao', 'posto_grad']

    def get_success_url(self):
        if self.get_object().id == self.request.user.pessoas.militar.id:
            return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pessoas.pk})
        else:
            return reverse('pessoas:cadastropessoa', kwargs={"pk": self.get_object().pessoas.pk})
