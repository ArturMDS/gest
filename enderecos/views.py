from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Endereco
from pessoas.models import Pessoa


class Criarendereco(LoginRequiredMixin, CreateView):
    template_name = "criarendereco.html"
    model = Endereco
    fields = ['logadouro', 'complemento', 'bairro', 'cep', 'cidade']

    def get_context_data(self, **kwargs):
        context = super(Criarendereco, self).get_context_data(**kwargs)
        data = {'id': self.request.GET['novo_id']}
        pessoa = Pessoa.objects.get(id=data['id'])
        context["pessoas"] = pessoa
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


class Perfilendereco(LoginRequiredMixin, UpdateView):
    template_name = "perfilendereco.html"
    model = Endereco
    fields = ['logadouro', 'complemento', 'bairro', 'cep', 'cidade']

    def get_success_url(self):
        if self.get_object().id == self.request.user.pessoas.endereco.id:
            return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pessoas.pk})
        else:
            return reverse('pessoas:cadastropessoa', kwargs={"pk": self.get_object().pessoas.pk})
