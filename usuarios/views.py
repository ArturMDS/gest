from django.shortcuts import reverse, redirect
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from .forms import CriarUsuarioForm, CriarAutoCadMilitarForm
from contatos.models import Contato
from pessoas.models import Pessoa
from documentos.models import Documento
from enderecos.models import Endereco
from militares.models import Militar, Atributos
from .function_usuarios import troca_su, acesso_om, acesso_su


class Homepage(LoginRequiredMixin, TemplateView):
    template_name = "homepage.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(Homepage, self).dispatch(request, *args, **kwargs)
        elif request.user.numero >= 6 and request.user.acesso != 'novo':
            return super(Homepage, self).dispatch(request, *args, **kwargs)
        elif request.user.numero <= 9 and request.user.acesso == 'novo':
            return redirect('usuarios:novo')
        else:
            return redirect('usuarios:autocaddone')


class Novo(LoginRequiredMixin, CreateView):
    template_name = "novo.html"
    model = Pessoa
    fields = ['nome_completo', 'data_nasc', 'foto',
              'nome_pai', 'nome_mae', 'peso',
              'fator_rh', 'tipo_sanguineo', 'altura',
              'escolaridade', 'religiao']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(Novo, self).dispatch(request, *args, **kwargs)
        elif request.user.numero >= 1:
            pk = request.user.pessoas.pk
            return redirect('usuarios:autocad', pk)
        else:
            return super(Novo, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class AutoCad(LoginRequiredMixin, DetailView):
    template_name = "autocad.html"
    model = Pessoa

    def dispatch(self, request, *args, **kwargs):
        if request.user.numero == 9:
            return redirect('usuarios:autocaddone')
        else:
            return super(AutoCad, self).dispatch(request, *args, **kwargs)


class AutoCadContato(LoginRequiredMixin, CreateView):
    template_name = "autocadcontato.html"
    model = Contato
    fields = ['telefone', 'celular']

    def form_valid(self, form):
        form.instance.pessoa = self.request.user.pessoas
        form.instance.email = self.request.user.email
        form.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class AutoCadDocumento(LoginRequiredMixin, CreateView):
    template_name = "autocaddocumento.html"
    model = Documento
    fields = ['rg', 'cpf', 'titulo_eleitor',
              'zona_eleitoral', 'secao_eleitoral',
              'cnh', 'cat_cnh', 'data_primeira_habilitacao']

    def form_valid(self, form):
        form.instance.pessoa = self.request.user.pessoas
        form.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class AutoCadEndereco(LoginRequiredMixin, CreateView):
    template_name = "autocadendereco.html"
    model = Endereco
    fields = ['logadouro', 'complemento', 'bairro', 'cep', 'cidade']

    def form_valid(self, form):
        form.instance.pessoa = self.request.user.pessoas
        form.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class AutoCadMilitar(LoginRequiredMixin, CreateView):
    template_name = "autocadmilitar.html"
    model = Militar
    form_class = CriarAutoCadMilitarForm

    def form_valid(self, form):
        form.instance.pessoa = self.request.user.pessoas
        form.instance.posto_grad = "Conscrito"
        form.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        militar = Militar.objects.last()
        militar.posto_grad = "Conscrito"
        atrib = Atributos.objects.create(militar=militar)
        atrib.save()
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class AutoCadDone(LoginRequiredMixin, TemplateView):
    template_name = "autocaddone.html"

    def dispatch(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super(AutoCadDone, self).dispatch(request, *args, **kwargs)


class ChangeDone(LoginRequiredMixin, TemplateView):
    template_name = "change_done.html"


class Perfil(LoginRequiredMixin, DetailView):
    template_name = "perfil.html"
    model = Usuario


class Perfilusuario(LoginRequiredMixin, UpdateView):
    template_name = "perfilusuario.html"
    model = Usuario
    fields = ['username', 'email']

    def get_success_url(self):
        return reverse('usuarios:perfil', kwargs={"pk": self.request.user.pk})


class Criarusuario(FormView):
    template_name = "criarusuario.html"
    form_class = CriarUsuarioForm

    def form_valid(self, form):
        contatos = Contato.objects.all()
        nr = int(len(contatos))
        cont = 0
        for contato in contatos:
            if contato.email == form.instance.email:
                form.instance.acesso = 'básico'
                form.instance.numero = 7
                form.save()
                contato.pessoa.usuario = Usuario.objects.last()
                contato.pessoa.save()
                cont -= 2
            cont += 1
        if nr == cont:
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:login')


class GestUsuario(LoginRequiredMixin, TemplateView):
    template_name = "gestusuario.html"

    def get_context_data(self, **kwargs):
        context = super(GestUsuario, self).get_context_data(**kwargs)
        pessoa = self.request.user.pessoas
        s1 = self.request.user.pessoas.militar.unidade.s1
        cmt_su = self.request.user.pessoas.militar.subunidade.cmt
        sgte = self.request.user.pessoas.militar.subunidade.sgte
        if pessoa == s1:
            om_logada = self.request.user.pessoas.militar.unidade
            militares = Militar.objects.filter(unidade=om_logada, pessoa__usuario__acesso="novo")
            context["militares"] = militares
            return context
        if (pessoa == cmt_su) or (pessoa == sgte):
            su_logada = self.request.user.pessoas.militar.subunidade
            militares = Militar.objects.filter(subunidade=su_logada, pessoa__usuario__acesso="novo")
            context["militares"] = militares
            return context


class ConfirmUsuario(LoginRequiredMixin, UpdateView):
    template_name = "confirmusuario.html"
    model = Usuario
    fields = []

    def get_success_url(self):
        usuario = Usuario.objects.get(id=self.object.id)
        usuario.acesso = "básico"
        usuario.numero += 1
        usuario.save()
        usuario.pessoas.situacao = "Ativo"
        usuario.pessoas.save()
        return reverse('usuarios:gestusuario')


class AllUsuario(LoginRequiredMixin, TemplateView):
    template_name = "allusuario.html"

    def get_context_data(self, **kwargs):
        context = super(AllUsuario, self).get_context_data(**kwargs)
        pessoa = self.request.user.pessoas
        s1 = self.request.user.pessoas.militar.unidade.s1
        cmt_su = self.request.user.pessoas.militar.subunidade.cmt
        sgte = self.request.user.pessoas.militar.subunidade.sgte
        if pessoa == s1:
            om_logada = self.request.user.pessoas.militar.unidade
            militares = Militar.objects.filter(unidade=om_logada)
            context["militares"] = militares
            return context
        if (pessoa == cmt_su) or (pessoa == sgte):
            su_logada = self.request.user.pessoas.militar.subunidade
            militares = Militar.objects.filter(subunidade=su_logada)
            context["militares"] = militares
            return context


class UpdateAutoCadPessoa(LoginRequiredMixin, UpdateView):
    template_name = "novo.html"
    model = Pessoa
    fields = ['nome_completo', 'data_nasc', 'foto',
              'nome_pai', 'nome_mae', 'peso',
              'fator_rh', 'tipo_sanguineo', 'altura',
              'escolaridade', 'religiao']

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class UpdateAutoCadContato(LoginRequiredMixin, UpdateView):
    template_name = "autocadcontato.html"
    model = Contato
    fields = ['telefone', 'celular']

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class UpdateAutoCadEndereco(LoginRequiredMixin, UpdateView):
    template_name = "autocadendereco.html"
    model = Endereco
    fields = ['logadouro', 'complemento', 'bairro', 'cep', 'cidade']

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class UpdateAutoCadDocumento(LoginRequiredMixin, UpdateView):
    template_name = "autocaddocumento.html"
    model = Documento
    fields = ['rg', 'cpf', 'titulo_eleitor',
              'zona_eleitoral', 'secao_eleitoral',
              'cnh', 'cat_cnh', 'data_primeira_habilitacao']

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class UpdateAutoCadMilitar(LoginRequiredMixin, UpdateView):
    template_name = "autocadmilitar.html"
    model = Militar
    form_class = CriarAutoCadMilitarForm

    def get_success_url(self):
        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


# TODO: acertar a automação funções/acessos
class GestFuncao(LoginRequiredMixin, TemplateView):
    template_name = "gestfuncao.html"

    def get_context_data(self, **kwargs):
        context = super(GestFuncao, self).get_context_data(**kwargs)
        pessoa = self.request.user.pessoas
        s1 = self.request.user.pessoas.militar.unidade.s1
        cmt_su = self.request.user.pessoas.militar.subunidade.cmt
        sgte = self.request.user.pessoas.militar.subunidade.sgte
        if pessoa == s1:
            om_logada = self.request.user.pessoas.militar.unidade
            subunidades = om_logada.subunidade.all()
            militares = Militar.objects.filter(unidade=om_logada, pessoa__situacao='Ativo')
            context["subunidades"] = subunidades
            context["militares"] = militares
            context["unidade"] = om_logada
            context["s1"] = s1
            context["cmt_su"] = cmt_su
            context["sgte"] = sgte
            return context
        if (pessoa == cmt_su) or (pessoa == sgte):
            su_logada = self.request.user.pessoas.militar.subunidade
            subunidades = self.request.user.pessoas.militar.unidade.subunidade.all()
            militares = Militar.objects.filter(subunidade=su_logada, pessoa__situacao='Ativo')
            context["subunidades"] = subunidades
            context["militares"] = militares
            context["subunidade"] = su_logada
            context["s1"] = s1
            context["cmt_su"] = cmt_su
            context["sgte"] = sgte
            return context

    def post(self, *args, **kwargs):
        dados = self.request.POST
        for dado in dados:
            if "_" in dado:
                if "subunidade" in dado:
                    if self.request.POST[dado] != '----------':
                        id_su = int(self.request.POST[dado])
                        id_mil = int(dado[dado.find("_")+1:])
                        troca_su(id_su, id_mil)
                elif "acessoom" in dado:
                    if self.request.POST[dado] != '----------':
                        id_mil = int(dado[dado.find("_")+1:])
                        funcao = self.request.POST[dado]
                        acesso_om(id_mil, funcao)
                elif "acessosu" in dado:
                    if self.request.POST[dado] != '----------':
                        id_mil = int(dado[dado.find("_")+1:])
                        funcao = self.request.POST[dado]
                        acesso_su(id_mil, funcao)
        return redirect('usuarios:gestfuncao')

