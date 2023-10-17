from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Viatura


class Viaturas(LoginRequiredMixin, ListView):
    template_name = "viatura.html"
    model = Viatura

    def get_context_data(self, **kwargs):
        context = super(Viaturas, self).get_context_data(**kwargs)
        viaturas = Viatura.objects.all()
        context["viaturas"] = viaturas
        return context


class Criarviatura(LoginRequiredMixin, CreateView):
    template_name = "criarviatura.html"
    model = Viatura
    fields = '__all__'

    def get_success_url(self):
        return reverse('viaturas:viatura')


class Updateviatura(LoginRequiredMixin, UpdateView):
    template_name = "updateviatura.html"
    model = Viatura
    fields = '__all__'

    def get_success_url(self):
        return reverse('viaturas:viatura')
