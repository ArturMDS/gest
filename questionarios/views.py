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


def auto_questionarioum(args):
    q = Questionarioum.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=pessoa.relatorio_cs.id)
    if q.pergunta_um == "Com os pais":
        q.pontos += 10
    elif q.pergunta_um == "Só com o pai":
        q.pontos += 7
    elif q.pergunta_um == "Só com a mãe":
        q.pontos += 7
    elif q.pergunta_um == "Com avós":
        q.pontos += 5
    elif q.pergunta_um == "Sozinho":
        q.pontos += 2
    else:
        q.obs += "\n- O senhor alega morar com o cônjuge, " \
                 "o senhor é casado? Quem é o provedor da casa?"
        r.sugestao = "Não deve Servir"
        q.parcial = "Não deve Servir"

    if q.pergunta_dois == "Junto":
        q.pontos += 10
    elif q.pergunta_um == "Perto":
        q.pontos += 5
    else:
        pass

    if q.pergunta_tres == "menos de 30min":
        q.pontos += 10
    elif q.pergunta_tres == "menos de 1h":
        q.pontos += 5
    elif q.pergunta_tres == "menos de 1h30min":
        q.pontos += 3
    else:
        q.obs += f"\n- O senhor alega que reside a mais de 1h30min do quartel, " \
                 f"o senhor reside em qual cidade?(Declarou que reside na " \
                 f"{q.pessoa.endereco.logadouro}, {q.pessoa.endereco.complemento}, " \
                 f"na cidade de {q.pessoa.endereco.cidade})"

    if q.pergunta_quatro == "Três ou mais irmãos":
        q.pontos += 5
    elif q.pergunta_quatro == "Dois irmãos":
        q.pontos += 3
    elif q.pergunta_quatro == "Apenas um(a) irmão(ã)":
        q.pontos += 2
    else:
        q.pontos += 1

    if q.pergunta_cinco == "Não":
        q.pontos += 20
    else:
        q.obs += f"\n- O senhor alega possuir filho(s) e que " \
                 f"reside {q.pergunta_um}, quem cuida da criança?."
        r.sugestao = "Não deve Servir"
        q.parcial = "Não deve Servir"

    if q.pergunta_seis == "Nenhum":
        q.pontos += 20
    else:
        q.obs += f"\n- O senhor alega ter problemas de {q.pergunta_seis}, " \
                 f"quando ocorreu a primeira vez? Ainda sente dores?"
        r.sugestao = "Não deve Servir"

    if q.pergunta_sete == "Sim":
        q.pontos += 20
        q.obs += f"\n- O senhor trabalhou (ou trabalha) na empresa {q.pergunta_oito} " \
                 f"na função de {q.pergunta_nove}? O que você faz(ou fazia)?"
        if r.sugestao != "Não deve Servir":
            r.sugestao = "Deve Servir"
            q.parcial = "Deve Servir"

    if q.parcial == "Sem Sugestão":
        q.parcial = "Pode Servir"
    q.save()
    q.pessoa.militar.atributos.ranking_inicial += q.pontos
    r.obs_questionario += q.obs
    q.pessoa.militar.atributos.save()
    r.save()


def auto_questionariodois(args):
    q = Questionariodois.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=pessoa.relatorio_cs.id)

    if q.pergunta_um == "Sim":
        q.pessoa.militar.atributos.ranking_inicial += 1

    if q.pergunta_dois == "Não":
        q.pontos += 1

    if q.pergunta_tres == "nem brinco, nem piercing":
        q.pontos += 5
    elif q.pergunta_tres == "Apenas piercing":
        q.pontos += 1
    elif q.pergunta_tres == "Apenas brinco":
        q.pontos += 1
    else:
        pass

    if q.pergunta_quatro == "Nenhum":
        q.pontos += 20
    else:
        q.obs += f"\n- O senhor alega possuir episódios de {q.pergunta_quatro}, " \
                 f"quando ocorreu a primeira vez? Ainda ocorre algum episódio?"
        r.sugestao = "Não deve Servir"
        q.parcial = "Não deve Servir"

    if q.pergunta_cinco == "Sim":
        q.pontos += 10
        q.obs += f"\n- O senhor alega que pratica {q.pergunta_seis}, " \
                 f"o senhor já foi federado? " \
                 f"Qual é a experiência que tem em cada um deles?"

    if q.pergunta_sete == "Nenhuma":
        q.pontos += 5
    elif q.pergunta_sete == "Uma tatuagem grande":
        q.pontos += 1
        q.obs += f"\n- O senhor alega possuir {q.pergunta_sete}, " \
                 f"em qual parte do corpo? Qual tipo de tatuagem (desenho)?"
    elif q.pergunta_sete == "Uma tatuagem pequena":
        q.pontos += 4
        q.obs += f"\n- O senhor alega possuir {q.pergunta_sete}, " \
                 f"em qual parte do corpo? Qual tipo de tatuagem (desenho)?"
    else:
        q.obs += f"\n- O senhor alega possuir {q.pergunta_sete}, " \
                 f"algumas delas é agressiva, discriminatória e/ou racista? " \
                 f"O senhor não se acha muito jovem para ter várias tatuagens?"

    if q.pergunta_oito == "Não":
        q.pontos += 2
    else:
        q.obs += f"\n- O senhor alega que gosta de sair para {q.pergunta_nove}, " \
                 f"faz isso com frequência? Tem algumm fonte de renda para custear?"

    if q.pergunta_dez == "Não":
        q.pontos += 20
    else:
        q.obs += "\n- O senhor alega possuir modificações corporais, em qual parte do corpo?"
        r.sugestao = "Não deve Servir"
        q.parcial = "Não deve Servir"

    if q.pergunta_onze == "Três ou mais":
        q.pontos += 10
        if r.sugestao != "Não deve Servir":
            r.sugestao = "Deve Servir"
        q.obs += f"\n- O senhor alega ter lido {q.pergunta_onze} " \
                 f"no ano passado? Qual foi o que mais gostou?"
    elif q.pergunta_onze == "Dois":
        q.pontos += 8
        q.obs += f"\n- O senhor alega ter lido {q.pergunta_onze} " \
                 f"no ano passado? Qual foi o que mais gostou?"
    elif q.pergunta_onze == "Apenas um":
        q.pontos += 6
    else:
        pass

    if q.pergunta_doze == "Não":
        q.pontos += 5
    else:
        q.obs += "\n- Qual tipo de grupo, " \
                 "sociedade torcida ou agremiação o senhor pertence?"

    if q.pergunta_treze == "Sim":
        q.pontos += 3
        if r.sugestao != "Não deve Servir":
            r.sugestao = "Deve Servir"
        q.obs += f"\n- Qual tipo de instrumento o senhor toca?"

    if q.pergunta_quatorze == "Não":
        q.pontos += 3

    if q.pergunta_quinze == "Não":
        q.pontos += 4

    if q.pergunta_dezesseis == "Não":
        q.pontos += 5
    else:
        q.obs += "\n- Qual foi o tipo e em " \
                 "qual situação o senhor usosu arma de fogo?"

    if q.pergunta_dezessete == "Não":
        q.pontos += 5

    if q.pergunta_dezoito == "Não":
        q.pontos += 20
    else:
        q.obs += "\n- O senhor alega que já consumiu drogas, qual tipo de droga? Ainda faz uso?"
        r.sugestao = "Não deve Servir"

    if q.pergunta_dezenove == "Nenhum":
        q.pontos += 5

    if q.pergunta_vinte == "Não":
        q.pontos += 5

    if q.pergunta_vinteum == "Não":
        q.pontos += 5

    if q.pergunta_vintedois == "Não":
        q.pontos += 5

    if q.pergunta_vintetres == "Nenhum":
        q.pontos += 10

    if q.pergunta_vintequatro == "Não":
        q.pontos += 10
    else:
        q.obs += "\n- O senhor foi acusado de qual crime?"
        r.sugestao = "Não deve Servir"
        q.parcial = "Não deve Servir"

    if q.pergunta_vintecinco == "Sim":
        q.pontos += 2

    if q.pergunta_vinteseis == "Sim":
        q.pontos += 10

    if q.pergunta_vintesete == "Não":
        q.pontos += 5
    else:
        q.obs += "\n- O senhor alega que tem motivos para não servir, quais são?"

    if q.parcial == "Sem Sugestão":
        q.parcial = "Pode Servir"
    q.save()
    q.pessoa.militar.atributos.ranking_inicial += q.pontos
    q.pessoa.militar.atributos.save()
    r.obs_questionario += q.obs
    r.save()


def auto_questionariotres(args):
    q = Questionariotres.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=pessoa.relatorio_cs.id)

    if q.pergunta_um == "Não":
        q.pontos += 10
    else:
        q.obs += f"\n- O senhor alega que quer ser laranjeira " \
                 f"(Mora em {q.pessoa.endereco.cidade}), por qual motivo?"

    if q.pergunta_dois == "Sim":
        q.pontos += 5
        if r.sugestao != "Não deve Servir":
            r.sugestao = "Deve Servir"
            q.parcial = "Deve Servir"
        q.obs += "\n- Qual outro idioma o senhor fala?"

    if q.pergunta_quatro == "Sim":
        q.pontos += 5

    if q.pergunta_cinco == "Sim":
        q.pontos += 10
        if r.sugestao != "Não deve Servir":
            r.sugestao = "Deve Servir"
            q.parcial = "Deve Servir"
        q.obs += f"\n- O senhor alega que ter ao mínimo interesse em {q.pergunta_seis} " \
                 f"O senhor tem alguma experiência em alguma dessa áreas?"

    if q.parcial == "Sem Sugestão":
        q.parcial = "Pode Servir"
    q.save()
    if r.sugestao == "Sem Sugestão":
        r.sugestao = "Pode Servir"
    q.pessoa.militar.atributos.ranking_inicial += q.pontos
    q.pessoa.militar.atributos.save()
    if r.obs_questionario == "Perguntas a serem feitas ao entrevistado:":
        r.obs_questionario = "Sem observações"
    r.obs_questionario += q.obs
    r.save()


def zera_questionarioum(args):
    q = Questionarioum.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=q.pessoa.relatorio_cs.id)
    pessoa.militar.atributos.ranking_inicial -= q.pontos
    q.pontos = 0
    r.obs_questionario = r.obs_questionario.replace(q.obs, "")
    q.obs = ""
    q.parcial = "Sem Sugestão"
    q.save()
    r.save()
    pessoa.militar.atributos.save()


def zera_questionariodois(args):
    q = Questionariodois.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=q.pessoa.relatorio_cs.id)
    pessoa.militar.atributos.ranking_inicial -= q.pontos
    q.pontos = 0
    r.obs_questionario = r.obs_questionario.replace(q.obs, "")
    q.obs = ""
    q.parcial = "Sem Sugestão"
    q.save()
    r.save()
    pessoa.militar.atributos.save()


def zera_questionariotres(args):
    q = Questionariotres.objects.get(id=args)
    pessoa = Pessoa.objects.get(id=q.pessoa.id)
    r = RelatorioCS.objects.get(id=q.pessoa.relatorio_cs.id)
    pessoa.militar.atributos.ranking_inicial -= q.pontos
    q.pontos = 0
    r.obs_questionario = r.obs_questionario.replace(q.obs, "")
    q.obs = ""
    q.parcial = "Sem Sugestão"
    q.save()
    r.save()
    pessoa.militar.atributos.save()


def define_relatorio(args):
    pessoa = Pessoa.objects.get(id=args)
    q1 = Questionarioum.objects.get(pessoa=pessoa)
    q2 = Questionariodois.objects.get(pessoa=pessoa)
    q3 = Questionariotres.objects.get(pessoa=pessoa)
    r = RelatorioCS.objects.get(pessoa=pessoa)

    if q1.parcial == "Não deve Servir" or q2.parcial == "Não deve Servir" \
            or q3.parcial == "Não deve Servir":
        r.sugestao = "Não deve Servir"
    elif (q1.parcial != "Não deve Servir" and q2.parcial != "Não deve Servir"
          and q3.parcial != "Não deve Servir") and \
            (q1.parcial == "Deve Servir" or q2.parcial == "Deve Servir"
             or q3.parcial == "Deve Servir"):
        r.sugestao = "Deve Servir"
    else:
        r.sugestao = "Pode Servir"
    r.save()


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

