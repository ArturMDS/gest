from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Documento
from pessoas.models import Pessoa


class Criardocumento(LoginRequiredMixin, CreateView):
    template_name = "criardocumento.html"
    model = Documento
    fields = ['rg', 'cpf', 'titulo_eleitor', 'cnh', 'cat_cnh']

    def get_context_data(self, **kwargs):
        context = super(Criardocumento, self).get_context_data(**kwargs)
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


class Perfildocumento(LoginRequiredMixin, UpdateView):
    template_name = "perfildocumento.html"
    model = Documento
    fields = ['rg', 'cpf', 'titulo_eleitor', 'cnh', 'cat_cnh']

    def get_success_url(self):
        if self.get_object().id == self.request.user.pessoas.documento.id:
            return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pessoas.pk})
        else:
            return reverse('pessoas:cadastropessoa', kwargs={"pk": self.get_object().pessoas.pk})
