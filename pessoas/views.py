from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Pessoa
from militares.models import Militar


class Cadastro(LoginRequiredMixin, ListView):
    template_name = "cadastro.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(Cadastro, self).get_context_data(**kwargs)
        if self.request.user.acesso == 'Estado Maior':
            om_logada = self.request.user.pessoas.militar.subunidade.OM
            militares = Militar.objects.filter(unidade=om_logada)
            context["militares"] = militares
            return context
        else:
            su_logada = self.request.user.pessoas.militar.subunidade
            militares = Militar.objects.filter(subunidade=su_logada).order_by("-posto_grad")
            context["militares"] = militares
            return context


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
