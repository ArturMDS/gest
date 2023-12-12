from django.shortcuts import reverse
from django.views.generic import ListView, \
    CreateView, \
    DetailView, \
    UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Observacao, Militar, Atributos, Destino
from .forms import CriarMilitarForm, \
    UpdateObservacaoForm, \
    PerfilMilitarForm, \
    UpdateDestinoForm, \
    CriarDestinoForm
from pessoas.models import Pessoa
from usuarios.function_usuarios import troca_su
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from datetime import datetime, timezone
from .function_militares import lista_transgre, define_pontos, define_atributos


class Fatosobservados(LoginRequiredMixin, ListView):
    template_name = "fatosobservados.html"
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super(Fatosobservados, self).get_context_data(**kwargs)
        pessoa = self.request.user.pessoas
        aux_s1 = self.request.user.pessoas.militar.unidade.acesso_s1.all()
        quadros = self.request.user.pessoas.militar.unidade.quadros.all()
        if (pessoa in quadros) or (pessoa in aux_s1):
            om_logada = self.request.user.pessoas.militar.unidade
            soldados = Militar.objects.filter(unidade=om_logada,
                                              pessoa__situacao="Ativo",
                                              posto_grad__icontains="Soldado").order_by('-posto_grad')
            cabos = Militar.objects.filter(unidade=om_logada,
                                           pessoa__situacao="Ativo",
                                           posto_grad__icontains="Cabo")
            context["soldados"] = soldados
            context["cabos"] = cabos
            return context


class Pesquisafatosobs(LoginRequiredMixin, ListView):
    template_name = "pesquisafatosobs.html"
    model = Militar

    def get_queryset(self):
        pesquisa = self.request.GET.get("query")
        pessoa = self.request.user.pessoas
        aux_s1 = self.request.user.pessoas.militar.unidade.acesso_s1.all()
        quadros = self.request.user.pessoas.militar.unidade.quadros.all()
        if pesquisa:
            if (pessoa in quadros) or (pessoa in aux_s1):
                om_logada = self.request.user.pessoas.militar.unidade
                object_list = self.model.objects.filter(pessoa__nome_completo__icontains=pesquisa,
                                                        unidade=om_logada,
                                                        pessoa__situacao="Ativo")
                return object_list
        else:
            return None


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
    form_class = CriarMilitarForm

    def get_context_data(self, **kwargs):
        context = super(Criarmilitar, self).get_context_data(**kwargs)
        data = {'id': self.request.GET['novo_id']}
        pessoa = Pessoa.objects.get(id=data['id'])
        context["pessoa"] = pessoa
        return context

    def get_form_kwargs(self):
        kwargs = super(Criarmilitar, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        data = {'id': self.request.GET['novo_id']}
        form.instance.pessoa = Pessoa.objects.get(id=data['id'])
        form.instance.unidade = self.request.user.pessoas.militar.unidade
        form.save()
        id_mil = Militar.objects.last().id
        id_su = Militar.objects.last().subunidade.id
        troca_su(id_su, id_mil)
        return super().form_valid(form)

    def get_success_url(self):
        militar = Militar.objects.last()
        atrib = Atributos.objects.create(militar=militar)
        atrib.save()
        data = {'id': self.request.GET['novo_id']}
        pessoa = Pessoa.objects.get(id=data['id'])
        return reverse('pessoas:cadastropessoa', kwargs={"pk": pessoa.id})


class Criarobservacao(LoginRequiredMixin, CreateView):
    template_name = "criarobservacao.html"
    model = Observacao
    fields = ['tipo', 'relato_fato']

    def form_valid(self, form):
        militar = Militar.objects.get(id=self.request.user.pessoas.militar.id)
        arrolado = Militar.objects.get(id=self.request.GET.get("arrolado"))
        form.instance.participante = militar
        form.instance.arrolado = arrolado
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Criarobservacao, self).get_context_data(**kwargs)
        militar = Militar.objects.get(id=self.request.GET.get("arrolado"))
        context["militar"] = militar
        return context

    def get_success_url(self):
        observacao = Observacao.objects.all().last()
        observacao.nr_processo = int(observacao.id) + 1
        observacao.save()
        return reverse('militares:fatosobservadospessoa', kwargs={"pk": observacao.arrolado.pessoa.id})


class Updateobservacao(LoginRequiredMixin, UpdateView):
    template_name = "updateobservacao.html"
    model = Observacao
    form_class = UpdateObservacaoForm

    def get_context_data(self, **kwargs):
        context = super(Updateobservacao, self).get_context_data(**kwargs)
        context["lista"] = lista_transgre
        return context

    def get_form_kwargs(self):
        kwargs = super(Updateobservacao, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        id_obs = self.get_object().id
        asks = self.request.POST
        define_pontos(id_obs)
        define_atributos(id_obs, asks)
        observacao = Observacao.objects.get(id=id_obs)
        return reverse('militares:fatosobservadospessoa', kwargs={"pk": observacao.arrolado.pessoa.id})


class Perfilmilitar(LoginRequiredMixin, UpdateView):
    template_name = "perfilmilitar.html"
    model = Militar
    form_class = PerfilMilitarForm

    def form_valid(self, form):
        id_mil = self.get_object().id
        id_su = form.instance.subunidade.id
        form.save()
        troca_su(id_su, id_mil)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(Perfilmilitar, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        if self.get_object().id == self.request.user.pessoas.militar.id:
            return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pessoas.pk})
        else:
            return reverse('pessoas:cadastropessoa', kwargs={"pk": self.get_object().pessoas.pk})


# TODO: mapa da força
class Verdestino(LoginRequiredMixin, ListView):
    template_name = "destino.html"
    model = Militar

    def dispatch(self, request, *args, **kwargs):
        om_logada = request.user.pessoas.militar.unidade
        militares = Militar.objects.filter(unidade=om_logada, pessoa__situacao="Ativo")
        hoje = datetime.now(timezone.utc)
        for militar in militares:
            destinos = militar.destino.all()
            for destino in destinos:
                if destino.check_out:
                    if (hoje < destino.check_out) and (hoje > destino.check_in):
                        if destino.in_force and not militar.is_present:
                            pass
                        else:
                            destino.in_force = True
                            militar.is_present = False
                            destino.save()
                            militar.save()
                    else:
                        if not destino.in_force and militar.is_present:
                            pass
                        else:
                            destino.in_force = False
                            militar.is_present = True
                            destino.save()
                            militar.save()
                else:
                    if destino.in_force and not militar.is_present:
                        pass
                    else:
                        destino.in_force = True
                        militar.is_present = False
                        destino.save()
                        militar.save()
        return super(Verdestino, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Verdestino, self).get_context_data(**kwargs)
        pessoa = self.request.user.pessoas
        s1 = self.request.user.pessoas.militar.unidade.s1
        aux_s1 = self.request.user.pessoas.militar.unidade.acesso_s1.all()
        cmt_su = self.request.user.pessoas.militar.subunidade.cmt
        quadros_su = self.request.user.pessoas.militar.subunidade.quadros.all()
        if (pessoa == s1) or (pessoa in aux_s1):
            om_logada = self.request.user.pessoas.militar.unidade
            destinos = Destino.objects.filter(militar__unidade=om_logada,
                                              in_force=True,
                                              militar__pessoa__situacao="Ativo")
            context["destinos"] = destinos
            context["s1"] = s1
            context["aux_s1"] = aux_s1
            return context
        elif (pessoa == cmt_su) or (pessoa in quadros_su):
            su_logada = self.request.user.pessoas.militar.subunidade
            destinos = Destino.objects.filter(militar__subunidade=su_logada,
                                               in_force=True,
                                               militar__pessoa__situacao="Ativo")
            context["destinos"] = destinos
            return context
        else:
            return None


class Criardestino(LoginRequiredMixin, CreateView):
    template_name = "criardestino.html"
    model = Destino
    form_class = CriarDestinoForm

    def get_form_kwargs(self):
        kwargs = super(Criardestino, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        hoje = datetime.now(timezone.utc)
        if form.instance.check_out:
            if (hoje > form.instance.check_out) or (hoje < form.instance.check_in):
                form.instance.in_force = False
        else:
            form.instance.in_force = True
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        destino = Destino.objects.last()
        if destino.in_force:
            destino.militar.is_present = False
        else:
            destino.militar.is_present = True
        destino.militar.save()
        return reverse('militares:destino')


class Updatedestino(LoginRequiredMixin, UpdateView):
    template_name = "updatedestino.html"
    model = Destino
    form_class = UpdateDestinoForm

    def get_form_kwargs(self):
        kwargs = super(Updatedestino, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        hoje = datetime.now(timezone.utc)
        if (hoje > form.instance.check_out) or (hoje < form.instance.check_in):
            form.instance.in_force = False
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        destino = Destino.objects.last()
        if destino.in_force:
            destino.militar.is_present = False
        else:
            destino.militar.is_present = True
        destino.militar.save()
        return reverse('militares:destino')


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Fatd(DetailView):
    template_name = "fatd.html"
    model = Observacao

    def get(self, request, *args, **kwargs):
        observacao = Observacao.objects.get(id=self.kwargs['pk'])
        hoje = datetime.now()
        params = {
            'observacao': observacao,
            'hoje': hoje,
            'request': request,
        }
        return Render.render('fatd.html', params, f'fatd_{observacao.arrolado}_{observacao.id}')


class Fdi(DetailView):
    template_name = "fdi.html"
    model = Militar

    def get(self, request, *args, **kwargs):
        militar = Militar.objects.get(id=self.kwargs['pk'])
        observacoes_neg = Observacao.objects.filter(arrolado=militar, tipo="negativa")
        observacoes_pos = Observacao.objects.filter(arrolado=militar, tipo="positiva")
        observacoes_neu = Observacao.objects.filter(arrolado=militar, tipo="neutra")
        params = {
            'militar': militar,
            'observacoes_neg': observacoes_neg,
            'observacoes_pos': observacoes_pos,
            'observacoes_neu': observacoes_neu,
            'request': request,
        }
        return Render.render('fdi.html', params, f'fdi_{militar.nome_guerra}')


class Mapaforca(ListView):
    template_name = "mapa_forca.html"
    model = Militar

    def get(self, request, *args, **kwargs):
        su = self.request.user.pessoas.militar.subunidade
        militares = Militar.objects.filter(subunidade=su)
        militares_1 = []
        militares_2 = []
        militares_3 = []

        for militar in militares:
            if (militar.posto_grad == "Coronel") or \
               (militar.posto_grad == "Tenente Coronel") or \
               (militar.posto_grad == "Major") or \
               (militar.posto_grad == "Capitão") or \
               (militar.posto_grad == "1º Tenente") or \
               (militar.posto_grad == "2º Tenente") or \
               (militar.posto_grad == "Aspirante à Oficial") or \
               (militar.posto_grad == "Subtenente") or \
               (militar.posto_grad == "1º Sargento") or \
               (militar.posto_grad == "2º Sargento") or \
               (militar.posto_grad == "3º Sargento"):
                militares_1.append(militar)
        for militar in militares:
            if (militar.posto_grad == "Cabo") or \
               (militar.posto_grad == "Soldado NB") or \
               (militar.posto_grad == "Soldado EV"):
                if len(militares_1) <= 57:
                    militares_1.append(militar)
                elif (len(militares_1) > 57) and (len(militares_2) <= 144):
                    militares_2.append(militar)
                else:
                    militares_3.append(militar)
        hoje = datetime.now()
        params = {
            'su': su,
            'militares_1': militares_1,
            'militares_2': militares_2,
            'militares_3': militares_3,
            'hoje': hoje,
            'request': request,
        }
        return Render.render('mapa_forca.html', params, f'mapa_da_forca_{su.abreviatura}')

