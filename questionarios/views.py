from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Questionarioum, Questionariodois, Questionariotres
from .forms import QuestionarioumForm, QuestionariodoisForm, QuestionariotresForm
from pessoas.models import Pessoa
from usuarios.models import Usuario


class Createquestionarioum(CreateView):
    template_name = "create_questionario_um.html"
    model = Questionarioum
    form_class = QuestionarioumForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        questionario.pessoa = pessoa
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionarioum.objects.last()
        if q.pergunta_um == "Com os pais":
            q.pessoa.militar.atributos.ranking_inicial += 10
        elif q.pergunta_um == "Só com o pai":
            q.pessoa.militar.atributos.ranking_inicial += 7
        elif q.pergunta_um == "Só com a mãe":
            q.pessoa.militar.atributos.ranking_inicial += 7
        elif q.pergunta_um == "Com avós":
            q.pessoa.militar.atributos.ranking_inicial += 5
        elif q.pergunta_um == "Sozinho":
            q.pessoa.militar.atributos.ranking_inicial += 2
        else:
            pass

        if q.pergunta_dois == "Junto":
            q.pessoa.militar.atributos.ranking_inicial += 10
        elif q.pergunta_um == "Perto":
            q.pessoa.militar.atributos.ranking_inicial += 5
        else:
            pass

        if q.pergunta_tres == "menos de 30min":
            q.pessoa.militar.atributos.ranking_inicial += 10
        elif q.pergunta_tres == "menos de 1h":
            q.pessoa.militar.atributos.ranking_inicial += 5
        elif q.pergunta_tres == "menos de 1h30min":
            q.pessoa.militar.atributos.ranking_inicial += 3
        else:
            pass

        if q.pergunta_quatro == "Três ou mais irmãos":
            q.pessoa.militar.atributos.ranking_inicial += 4
        elif q.pergunta_quatro == "Dois irmãos":
            q.pessoa.militar.atributos.ranking_inicial += 3
        elif q.pergunta_quatro == "Apenas um(a) irmão(ã)":
            q.pessoa.militar.atributos.ranking_inicial += 2
        else:
            q.pessoa.militar.atributos.ranking_inicial += 1

        if q.pergunta_cinco == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 20

        if q.pergunta_seis == "Nenhum":
            q.pessoa.militar.atributos.ranking_inicial += 20

        q.pessoa.militar.atributos.save()

        return reverse('questionarios:create_questionario_dois')


class Createquestionariodois(CreateView):
    template_name = "create_questionario_dois.html"
    model = Questionariodois
    form_class = QuestionariodoisForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        questionario.pessoa = pessoa
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionariodois.objects.last()
        if q.pergunta_um == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 1

        if q.pergunta_dois == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 1

        if q.pergunta_tres == "nem brinco, nem piercing":
            q.pessoa.militar.atributos.ranking_inicial += 5
        elif q.pergunta_tres == "Apenas piercing":
            q.pessoa.militar.atributos.ranking_inicial += 1
        elif q.pergunta_tres == "Apenas brinco":
            q.pessoa.militar.atributos.ranking_inicial += 1
        else:
            pass

        if q.pergunta_quatro == "Nenhum":
            q.pessoa.militar.atributos.ranking_inicial += 20

        if q.pergunta_cinco == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_sete == "Nenhuma":
            q.pessoa.militar.atributos.ranking_inicial += 5
        elif q.pergunta_sete == "Uma tatuagem grande":
            q.pessoa.militar.atributos.ranking_inicial += 1
        elif q.pergunta_sete == "Uma tatuagem pequena":
            q.pessoa.militar.atributos.ranking_inicial += 4
        else:
            pass

        if q.pergunta_oito == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 2

        if q.pergunta_dez == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 20

        if q.pergunta_onze == "Três ou mais":
            q.pessoa.militar.atributos.ranking_inicial += 10
        elif q.pergunta_onze == "Dois":
            q.pessoa.militar.atributos.ranking_inicial += 8
        elif q.pergunta_onze == "Apenas um":
            q.pessoa.militar.atributos.ranking_inicial += 6
        else:
            pass

        if q.pergunta_doze == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 5

        if q.pergunta_treze == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 3

        if q.pergunta_quatorze == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 3

        if q.pergunta_quinze == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 4

        if q.pergunta_dezesseis == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_dezessete == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_dezoito == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 20

        if q.pergunta_dezenove == "Nenhum":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_vinte == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 5

        if q.pergunta_vinteum == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_vintedois == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 5

        if q.pergunta_vintetres == "Nenhum":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_vintequatro == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_vintecinco == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 2

        if q.pergunta_vinteseis == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_vintesete == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 5

        q.pessoa.militar.atributos.save()

        return reverse('questionarios:create_questionario_tres')


class Createquestionariotres(CreateView):
    template_name = "create_questionario_tres.html"
    model = Questionariotres
    form_class = QuestionariotresForm

    def form_valid(self, form):
        questionario = form.save(commit=False)
        pessoa = Pessoa.objects.get(id=self.request.user.pessoas.id)
        questionario.pessoa = pessoa
        questionario.save()
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.numero += 1
        usuario.save()
        return super().form_valid(form)

    def get_success_url(self):
        q = Questionariotres.objects.last()
        if q.pergunta_um == "Não":
            q.pessoa.militar.atributos.ranking_inicial += 10

        if q.pergunta_dois == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 5

        if q.pergunta_quatro == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 5

        if q.pergunta_cinco == "Sim":
            q.pessoa.militar.atributos.ranking_inicial += 10

        q.pessoa.militar.atributos.save()

        return reverse('usuarios:autocad', kwargs={"pk": self.request.user.pessoas.pk})

