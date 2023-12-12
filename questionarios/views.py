from django.shortcuts import reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Questionarioum, \
    Questionariodois, \
    Questionariotres, \
    RelatorioCS
from .forms import QuestionarioumForm, \
    QuestionariodoisForm, \
    QuestionariotresForm, \
    UpdateQuestionariodoisForm, \
    UpdateQuestionariotresForm
from pessoas.models import Pessoa
from usuarios.models import Usuario
from .function_questionarios import auto_questionarioum, \
    auto_questionariodois, \
    auto_questionariotres, \
    zera_questionarioum, \
    zera_questionariodois, \
    zera_questionariotres, \
    define_relatorio


class Createquestionarioum(LoginRequiredMixin, CreateView):
    template_name = "create_questionario_um.html"
    model = Questionarioum
    form_class = QuestionarioumForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        relatorio = RelatorioCS.objects.create(pessoa=pessoa)
        relatorio.save()
        questionario.pessoa = pessoa
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionarioum.objects.last()
        auto_questionarioum(q.id)
        return reverse('questionarios:create_questionario_dois')


class Createquestionariodois(LoginRequiredMixin, CreateView):
    template_name = "create_questionario_dois.html"
    model = Questionariodois
    form_class = QuestionariodoisForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        questionario.pessoa = pessoa
        questionario.pergunta_seis = questionario.pergunta_seis.replace("'", "").replace("[", "").replace("]", "")
        questionario.pergunta_nove = questionario.pergunta_nove.replace("'", "").replace("[", "").replace("]", "")
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionariodois.objects.last()
        auto_questionariodois(q.id)
        return reverse('questionarios:create_questionario_tres')


class Createquestionariotres(LoginRequiredMixin, CreateView):
    template_name = "create_questionario_tres.html"
    model = Questionariotres
    form_class = QuestionariotresForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        questionario.pessoa = pessoa
        questionario.pergunta_seis = questionario.pergunta_seis.replace("'", "").replace("[", "").replace("]", "")
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionariotres.objects.last()
        auto_questionariotres(q.id)
        return reverse('usuarios:autocad', kwargs={"pk": q.pessoa.id})


class Updatequestionarioum(LoginRequiredMixin, UpdateView):
    template_name = "create_questionario_um.html"
    model = Questionarioum
    form_class = QuestionarioumForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionarioum(pessoa.questionario_um.id)
        auto_questionarioum(pessoa.questionario_um.id)
        define_relatorio(pessoa.id)

        return reverse('usuarios:autocad', kwargs={"pk": pessoa.pk})


class Updatequestionariodois(LoginRequiredMixin, UpdateView):
    template_name = "create_questionario_dois.html"
    model = Questionariodois
    form_class = QuestionariodoisForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionariodois(pessoa.questionario_dois.id)
        auto_questionariodois(pessoa.questionario_dois.id)
        define_relatorio(pessoa.id)

        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class Updatequestionariotres(LoginRequiredMixin, UpdateView):
    template_name = "create_questionario_tres.html"
    model = Questionariotres
    form_class = QuestionariotresForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionariotres(pessoa.questionario_tres.id)
        auto_questionariotres(pessoa.questionario_tres.id)
        define_relatorio(pessoa.id)

        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})


class Updateum(LoginRequiredMixin, UpdateView):
    template_name = "update_questionario_um.html"
    model = Questionarioum
    form_class = QuestionarioumForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionarioum(pessoa.questionario_um.id)
        auto_questionarioum(pessoa.questionario_um.id)
        define_relatorio(pessoa.id)

        return reverse('pessoas:listconscrito')


class Updatedois(LoginRequiredMixin, UpdateView):
    template_name = "update_questionario_dois.html"
    model = Questionariodois
    form_class = UpdateQuestionariodoisForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionariodois(pessoa.questionario_dois.id)
        auto_questionariodois(pessoa.questionario_dois.id)
        define_relatorio(pessoa.id)

        return reverse('pessoas:listconscrito')


class Updatetres(LoginRequiredMixin, UpdateView):
    template_name = "update_questionario_tres.html"
    model = Questionariotres
    form_class = UpdateQuestionariotresForm

    def get_success_url(self):
        pessoa = Pessoa.objects.get(id=self.object.pessoa.id)
        zera_questionariotres(pessoa.questionario_tres.id)
        auto_questionariotres(pessoa.questionario_tres.id)
        define_relatorio(pessoa.id)

        return reverse('pessoas:listconscrito')

