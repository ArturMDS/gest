from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Pessoa
from militares.views import Render
from militares.models import Militar
from questionarios.models import RelatorioCS
import locale
from datetime import datetime
from math import ceil


class Cadastro(LoginRequiredMixin, ListView):
    template_name = "cadastro.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(Cadastro, self).get_context_data(**kwargs)
        if self.request.user.acesso == 'Estado Maior':
            om_logada = self.request.user.pessoas.militar.unidade
            militares = Militar.objects.filter(unidade=om_logada).order_by("-posto_grad")
            context["militares"] = militares
            return context
        else:
            su_logada = self.request.user.pessoas.militar.subunidade
            militares = Militar.objects.filter(subunidade=su_logada).order_by("-posto_grad")
            context["militares"] = militares
            return context


class Pesquisacadastro(LoginRequiredMixin, ListView):
    template_name = "pesquisacadastro.html"
    model = Militar

    def get_queryset(self):
        pesquisa = self.request.GET.get("query")
        if pesquisa:
            if self.request.user.acesso == 'Estado Maior':
                om_logada = self.request.user.pessoas.militar.unidade
                object_list = self.model.objects.filter(pessoa__nome_completo__icontains=pesquisa, unidade=om_logada)
                return object_list
            else:
                su_logada = self.request.user.pessoas.militar.subunidade
                object_list = self.model.objects.filter(pessoa__nome_completo__icontains=pesquisa, subunidade=su_logada)
                return object_list
        else:
            return None


class Cadastropessoa(LoginRequiredMixin, DetailView):
    template_name = "cadastropessoa.html"
    model = Pessoa


class Criarpessoa(LoginRequiredMixin, CreateView):
    template_name = "criarpessoa.html"
    model = Pessoa
    fields = ['nome_completo', 'data_nasc', 'foto', 'nome_pai', 'nome_mae', 'peso', 'fator_rh', 'tipo_sanguineo',
              'altura', 'escolaridade', 'religiao']

    def form_valid(self, form):
        form.instance.situacao = "Ativo"
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pessoa = Pessoa.objects.all().last()
        return reverse('pessoas:cadastropessoa', kwargs={"pk": pessoa.id})


class Delete(LoginRequiredMixin, UpdateView):
    template_name = "delete.html"
    model = Pessoa
    fields = []

    def form_valid(self, form):
        form.instance.situacao = "Arquivo"
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pessoas:cadastro')


class Perfilpessoa(LoginRequiredMixin, UpdateView):
    template_name = "perfilpessoa.html"
    model = Pessoa
    fields = ['nome_completo', 'data_nasc', 'foto', 'nome_pai', 'nome_mae', 'peso', 'fator_rh', 'tipo_sanguineo',
              'altura', 'escolaridade', 'religiao']

    def get_success_url(self):
        if self.get_object().id == self.request.user.pessoas.id:
            return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pessoas.pk})
        else:
            return reverse('pessoas:cadastropessoa', kwargs={"pk": self.get_object().pk})


class ListConscrito(LoginRequiredMixin, ListView):
    template_name = "list_conscrito.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(ListConscrito, self).get_context_data(**kwargs)
        if self.request.user.acesso == 'Estado Maior':
            om_logada = self.request.user.pessoas.militar.unidade
            c = Militar.objects.filter(unidade=om_logada, posto_grad='Conscrito')
            conscritos = c.order_by('-atributos__ranking_inicial')
            context["conscritos"] = conscritos
            return context
        elif self.request.user.acesso == 'Sargenteante' or self.request.user.acesso == 'Comandante':
            su_logada = self.request.user.pessoas.militar.subunidade
            c = Militar.objects.filter(subunidade=su_logada, posto_grad='Conscrito')
            conscritos = c.order_by('-atributos__ranking_inicial')
            context["conscritos"] = conscritos
            return context


class ReadConscrito(LoginRequiredMixin, UpdateView):
    template_name = 'read_conscrito.html'
    model = RelatorioCS
    fields = ['obs_entrevistador']

    def form_valid(self, form):
        militar = Militar.objects.get(id=self.request.user.pessoas.militar.id)
        relatorio = form.save(commit=False)
        relatorio.entrevistador = militar
        relatorio.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ReadConscrito, self).get_context_data(**kwargs)
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        ri = pessoa.militar.atributos.ranking_inicial
        numero = ceil(ri/3)
        context["numero"] = numero
        return context

    def get_success_url(self):
        return reverse('pessoas:listconscrito')


class Formulario(DetailView):
    template_name = "formulario_cs.html"
    model = Pessoa

    def get(self, request, *args, **kwargs):
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        pessoa = Pessoa.objects.get(id=self.kwargs['pk'])
        hoje = datetime.now()
        data = hoje.strftime("%d de %B de %Y")
        params = {
            'pessoa': pessoa,
            'hoje': hoje,
            'data': data,
            'request': request,
        }
        return Render.render('formulario_cs.html', params, f'formulario_{pessoa.id}')

