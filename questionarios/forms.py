from django.forms import ModelForm
from .models import Questionarioum, Questionariodois, Questionariotres
from django import forms


class QuestionarioumForm(forms.ModelForm):

    LISTA_RESPOSTA1 = [
        ("Com os pais", "Com os pais"),
        ("Só com o pai", "Só com o pai"),
        ("Só com a mãe", "Só com a mãe"),
        ("Com avós", "Com avós"),
        ("Sozinho", "Sozinho"),
        ("Com cônjuge", "Com cônjuge")
    ]
    pergunta_um = forms.ChoiceField(
        label="Atualmente, com quem o senhor reside?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA1
    )

    LISTA_RESPOSTA2 = [
        ("Junto", "Junto"),
        ("Perto", "Perto"),
        ("Longe", "Longe")
    ]
    pergunta_dois = forms.ChoiceField(
        label="Durante sua infância ou adolescência, o senhor foi criado longe dos pais?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA2
    )

    LISTA_RESPOSTA3 = [
        ("menos de 30min", "menos de 30min"),
        ("menos de 1h", "menos de 1h"),
        ("menos de 1h30min", "menos de 1h30min"),
        ("mais de 1h30min", "mais de 1h30min"),
    ]
    pergunta_tres = forms.ChoiceField(
        label="Caso convocado para cumprir o serviço militar obrigatório, "
              "do local onde reside atualmente, "
              "quanto tempo o senhor demora para chegar neste quartel?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA3
    )

    LISTA_RESPOSTA4 = [
        ("Nenhum", "Nenhum"),
        ("Apenas um(a) irmão(ã)", "Apenas um(a) irmão(ã)"),
        ("Dois irmãos", "Dois irmãos"),
        ("Três ou mais irmãos", "Três ou mais irmãos")
    ]
    pergunta_quatro = forms.ChoiceField(
        label="O senhor possui quantos irmãos e irmãs no total? (sem contar o senhor)",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA4
    )

    LISTA_RESPOSTA_SN = [
        ("Sim", "Sim"),
        ("Não", "Não")
    ]
    pergunta_cinco = forms.ChoiceField(
        label="O senhor já tem filho(s)? (O senhor é pai?)",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA6 = [
        ("Nenhum", "Nenhum"),
        ("Coluna", "Coluna"),
        ("Joelho", "Joelho"),
        ("Tornozelo", "Tornozelo")
    ]
    pergunta_seis = forms.ChoiceField(
        label="O senhor já apresentou problemas físicos em alguma das seguintes partes do corpo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA6)

    pergunta_sete = forms.ChoiceField(
        label="O senhor já trabalhou ou trabalha atualmente?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_oito = forms.CharField(
        label="Qual é o nome da Empresa?", required=False)

    pergunta_nove = forms.CharField(
        label="Qual era a sua função?", required=False)

    pergunta_dez = forms.CharField(
        label="Endereço e/ou Telefone da Empresa?", required=False)

    class Meta:
        model = Questionarioum
        fields = ['pergunta_um', 'pergunta_dois', 'pergunta_tres',
                  'pergunta_quatro', 'pergunta_cinco', 'pergunta_seis',
                  'pergunta_sete', 'pergunta_oito', 'pergunta_nove', 'pergunta_dez']


class QuestionariodoisForm(forms.ModelForm):

    LISTA_RESPOSTA_SN = [
        ("Sim", "Sim"),
        ("Não", "Não")
    ]
    pergunta_um = forms.ChoiceField(
        label="O senhor é voluntário para servir?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dois = forms.ChoiceField(
        label="O senhor tem namorada?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA3 = [
        ("nem brinco, nem piercing", "nem brinco, nem piercing"),
        ("Apenas piercing", "Apenas piercing"),
        ("Apenas brinco", "Apenas brinco"),
        ("Ambos, brinco e piercing", "Ambos, brinco e piercing"),
    ]
    pergunta_tres = forms.ChoiceField(
        label="O senhor usa brinco? Possui piercing no corpo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA3)

    LISTA_RESPOSTA4 = [
        ("Nenhum", "Nenhum"),
        ("Depressão", "Depressão"),
        ("Transtornos psicológicos", "Transtornos psicológicos"),
        ("Intenção suicida", "Intenção suicida")
    ]
    pergunta_quatro = forms.ChoiceField(
        label="O senhor apresenta ou já apresentou algum dos seguintes episódios?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA4)

    pergunta_cinco = forms.ChoiceField(
        label="O senhor pratica algum esporte?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA6 = [
        ("Nenhum", "Nenhum"),
        ("Futebol", "Futebol"),
        ("Basquete", "Basquete"),
        ("Musculação", "Musculação"),
        ("Orientação", "Orientação"),
        ("Vôlei", "Vôlei"),
        ("Esportes Radicais", "Esportes Radicais"),
        ("Natação", "Natação"),
        ("Corrida", "Corrida"),
        ("Artes Marciais", "Artes Marciais"),
        ("Capoeira", "Capoeira"),
        ("Ciclismo", "Ciclismo")
    ]
    pergunta_seis = forms.MultipleChoiceField(
        label="Que tipo de esporte o senhor pratica?",
        widget=forms.CheckboxSelectMultiple, choices=LISTA_RESPOSTA6, required=False)

    LISTA_RESPOSTA7 = [
        ("Nenhuma", "Nenhuma"),
        ("Uma tatuagem grande", "Uma tatuagem grande"),
        ("Uma tatuagem pequena", "Uma tatuagem pequena"),
        ("Várias tatuagens", "Várias tatuagens")
    ]

    pergunta_sete = forms.ChoiceField(
        label="O senhor tem tatuagem pelo corpo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA7)

    pergunta_oito = forms.ChoiceField(
        label="O senhor costuma sair à noite?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA9 = [
        ("Danceteria", "Danceteria"),
        ("Bar", "Bar"),
        ("Restaurante", "Restaurante"),
        ("Estádio de Futebol", "Estádio de Futebol"),
        ("Cinema", "Cinema"),
        ("Eventos de Música", "Eventos de Música"),
        ("Teatro", "Teatro"),
        ("Igreja/Mesquita/Sinagoga e afins", "Igreja/Mesquita/Sinagoga e afins")
    ]

    pergunta_nove = forms.MultipleChoiceField(
        label="Que locais o senhor costuma frequentar?",
        widget=forms.CheckboxSelectMultiple, choices=LISTA_RESPOSTA9, required=False)

    pergunta_dez = forms.ChoiceField(
        label="O senhor possui alguma alteração corporal (body mod)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA11 = [
        ("Nenhum", "Nenhum"),
        ("Apenas um", "Apenas um"),
        ("Dois", "Dois"),
        ("Três ou mais", "Três ou mais")
    ]

    pergunta_onze = forms.ChoiceField(
        label="Ao longo do último ano, quantos livros o senhor leu?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_doze = forms.ChoiceField(
        label="O senhor participa de algum grupo, sociedade, torcida ou agremiação?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_treze = forms.ChoiceField(
        label="O senhor toca algum instrumento?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_quatorze = forms.ChoiceField(
        label="O senhor já experimentou bebida alcoólica?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_quinze = forms.ChoiceField(
        label="O senhor senhor fuma algum tipo de cigarro?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezesseis = forms.ChoiceField(
        label="O senhor já usou arma de fogo (revólver, pistola, fuzil, etc)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezessete = forms.ChoiceField(
        label="O senhor já ficou embriagado?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezoito = forms.ChoiceField(
        label="O senhor já experimentou algum tipo de droga (maconha, cocaína, etc)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezenove = forms.ChoiceField(
        label="O senhor possui quantos amigos que consomem bebida alcoólica?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_vinte = forms.ChoiceField(
        label="O senhor já se envolveu em briga?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vinteum = forms.ChoiceField(
        label="O senhor possui algum amigo que tenha arma de fogo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintedois = forms.ChoiceField(
        label="O senhor já teve que comparecer em uma delegacia como vítima de algum crime?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintetres = forms.ChoiceField(
        label="O senhor possui algum amigo que consuma drogas (maconha, cocaína, etc)? Quantos?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_vintequatro = forms.ChoiceField(
        label="O senhor já teve que comparecer em uma delegacia por estar sendo acusado de algum crime?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintecinco = forms.ChoiceField(
        label="O senhor possui algum amigo de etnia diferente da sua?\n"
              "(EX: se branco, amigo afrodescendente; Se afro, amigo branco)",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vinteseis = forms.ChoiceField(
        label="O senhor seria capaz de fazer amizade com uma pessoa com etnia diferente da sua?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintesete = forms.ChoiceField(
        label="O senhor julga que tenha algum motivo que o possa atrapalhar, ou impedir, de servir?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    class Meta:
        model = Questionariodois
        fields = ['pergunta_um', 'pergunta_dois', 'pergunta_tres',
                  'pergunta_quatro', 'pergunta_cinco', 'pergunta_seis',
                  'pergunta_sete', 'pergunta_oito', 'pergunta_nove', 'pergunta_dez',
                  'pergunta_onze', 'pergunta_doze', 'pergunta_treze',
                  'pergunta_quatorze', 'pergunta_quinze', 'pergunta_dezesseis',
                  'pergunta_dezessete', 'pergunta_dezoito', 'pergunta_dezenove', 'pergunta_vinte',
                  'pergunta_vinteum', 'pergunta_vintedois', 'pergunta_vintetres',
                  'pergunta_vintequatro', 'pergunta_vintecinco', 'pergunta_vinteseis',
                  'pergunta_vintesete']


class QuestionariotresForm(forms.ModelForm):

    LISTA_RESPOSTA_SN = [
        ("Sim", "Sim"),
        ("Não", "Não")
    ]
    pergunta_um = forms.ChoiceField(
        label="Caso incorporado, o senhor pretende morar no quartel?\n"
              "Tal situação é conhecida como laranjeira",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dois = forms.ChoiceField(
        label="O senhor sabe falar algum outro idioma, além do português?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_tres = forms.CharField(
        label="Caso incorporado, quais são as expectativas do senhor para o serviço militar?")

    pergunta_quatro = forms.ChoiceField(
        label="O senhor possui algum parente que seja militar?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_cinco = forms.ChoiceField(
        label="O senhor possui alguma habilidade profissional, curso técnico ou área de interesse?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA6 = [
        ("Mecânico de automóvel", "Mecânico de automóvel"),
        ("Eletricista de automóvel", "Eletricista de automóvel"),
        ("Motorista", "Motorista"),
        ("Carpínteiro", "Carpínteiro"),
        ("Pintor Predial", "Pintor Predial"),
        ("Servente de pedreiro", "Servente de pedreiro"),
        ("Manutenção de computador", "Manutenção de computador"),
        ("Torneiro Mecânico", "Torneiro Mecânico"),
        ("Agricultor", "Agricultor"),
        ("Digitador/Operador de micro", "Digitador/Operador de micro"),
        ("Cozinheiro", "Cozinheiro"),
        ("Técnico em refrigeração", "Técnico em refrigeração"),
        ("Cantor", "Cantor"),
        ("Lanterneiro", "Lanterneiro"),
        ("Pedreiro", "Pedreiro"),
        ("Soldador", "Soldador"),
        ("Serralheiro", "Serralheiro"),
        ("Eletricista Predial", "Eletricista Predial"),
        ("Programador de computador", "Programador de computador"),
        ("Alfaiate/Correeiro", "Alfaiate/Correeiro"),
        ("Piscineiro", "Piscineiro"),
        ("Encanador", "Encanador"),
        ("Garçom", "Garçom"),
        ("Estoquista", "Estoquista"),
        ("Auxiliar Contábil", "Auxiliar Contábil"),
        ("Auxiliar Administração", "Auxiliar Administração"),
        ("Telhadista", "Telhadista"),
        ("Jardineiro", "Jardineiro")
    ]
    pergunta_seis = forms.MultipleChoiceField(
        label="Que habilidades profissionais (ou área de interesse) o senhor julga possuir?",
        widget=forms.CheckboxSelectMultiple, choices=LISTA_RESPOSTA6, required=False)

    class Meta:
        model = Questionariotres
        fields = ['pergunta_um', 'pergunta_dois', 'pergunta_tres',
                  'pergunta_quatro', 'pergunta_cinco', 'pergunta_seis']


class UpdateQuestionariodoisForm(forms.ModelForm):
    LISTA_RESPOSTA_SN = [
        ("Sim", "Sim"),
        ("Não", "Não")
    ]
    pergunta_um = forms.ChoiceField(
        label="O senhor é voluntário para servir?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dois = forms.ChoiceField(
        label="O senhor tem namorada?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA3 = [
        ("nem brinco, nem piercing", "nem brinco, nem piercing"),
        ("Apenas piercing", "Apenas piercing"),
        ("Apenas brinco", "Apenas brinco"),
        ("Ambos, brinco e piercing", "Ambos, brinco e piercing"),
    ]
    pergunta_tres = forms.ChoiceField(
        label="O senhor usa brinco? Possui piercing no corpo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA3)

    LISTA_RESPOSTA4 = [
        ("Nenhum", "Nenhum"),
        ("Depressão", "Depressão"),
        ("Transtornos psicológicos", "Transtornos psicológicos"),
        ("Intenção suicida", "Intenção suicida")
    ]
    pergunta_quatro = forms.ChoiceField(
        label="O senhor apresenta ou já apresentou algum dos seguintes episódios?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA4)

    pergunta_cinco = forms.ChoiceField(
        label="O senhor pratica algum esporte?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA7 = [
        ("Nenhuma", "Nenhuma"),
        ("Uma tatuagem grande", "Uma tatuagem grande"),
        ("Uma tatuagem pequena", "Uma tatuagem pequena"),
        ("Várias tatuagens", "Várias tatuagens")
    ]

    pergunta_sete = forms.ChoiceField(
        label="O senhor tem tatuagem pelo corpo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA7)

    pergunta_oito = forms.ChoiceField(
        label="O senhor costuma sair à noite?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dez = forms.ChoiceField(
        label="O senhor possui alguma alteração corporal (body mod)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    LISTA_RESPOSTA11 = [
        ("Nenhum", "Nenhum"),
        ("Apenas um", "Apenas um"),
        ("Dois", "Dois"),
        ("Três ou mais", "Três ou mais")
    ]

    pergunta_onze = forms.ChoiceField(
        label="Ao longo do último ano, quantos livros o senhor leu?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_doze = forms.ChoiceField(
        label="O senhor participa de algum grupo, sociedade, torcida ou agremiação?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_treze = forms.ChoiceField(
        label="O senhor toca algum instrumento?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_quatorze = forms.ChoiceField(
        label="O senhor já experimentou bebida alcoólica?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_quinze = forms.ChoiceField(
        label="O senhor senhor fuma algum tipo de cigarro?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezesseis = forms.ChoiceField(
        label="O senhor já usou arma de fogo (revólver, pistola, fuzil, etc)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezessete = forms.ChoiceField(
        label="O senhor já ficou embriagado?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezoito = forms.ChoiceField(
        label="O senhor já experimentou algum tipo de droga (maconha, cocaína, etc)?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dezenove = forms.ChoiceField(
        label="O senhor possui quantos amigos que consomem bebida alcoólica?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_vinte = forms.ChoiceField(
        label="O senhor já se envolveu em briga?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vinteum = forms.ChoiceField(
        label="O senhor possui algum amigo que tenha arma de fogo?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintedois = forms.ChoiceField(
        label="O senhor já teve que comparecer em uma delegacia como vítima de algum crime?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintetres = forms.ChoiceField(
        label="O senhor possui algum amigo que consuma drogas (maconha, cocaína, etc)? Quantos",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA11)

    pergunta_vintequatro = forms.ChoiceField(
        label="O senhor já teve que comparecer em uma delegacia por estar sendo acusado de algum crime?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintecinco = forms.ChoiceField(
        label="O senhor possui algum amigo de etnia diferente da sua?\n"
              "(EX: se branco, amigo afrodescendente; Se afro, amigo branco)",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vinteseis = forms.ChoiceField(
        label="O senhor seria capaz de fazer amizade com uma pessoa com etnia diferente da sua?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_vintesete = forms.ChoiceField(
        label="O senhor julga que tenha algum motivo que o possa atrapalhar, ou impedir, de servir?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    class Meta:
        model = Questionariodois
        fields = ['pergunta_um', 'pergunta_dois', 'pergunta_tres',
                  'pergunta_quatro', 'pergunta_cinco', 'pergunta_sete',
                  'pergunta_oito', 'pergunta_dez', 'pergunta_onze',
                  'pergunta_doze', 'pergunta_treze', 'pergunta_quatorze',
                  'pergunta_quinze', 'pergunta_dezesseis', 'pergunta_dezessete',
                  'pergunta_dezoito', 'pergunta_dezenove', 'pergunta_vinte',
                  'pergunta_vinteum', 'pergunta_vintedois', 'pergunta_vintetres',
                  'pergunta_vintequatro', 'pergunta_vintecinco', 'pergunta_vinteseis',
                  'pergunta_vintesete']


class UpdateQuestionariotresForm(forms.ModelForm):
    LISTA_RESPOSTA_SN = [
        ("Sim", "Sim"),
        ("Não", "Não")
    ]
    pergunta_um = forms.ChoiceField(
        label="Caso incorporado, o senhor pretende morar no quartel?\n"
              "Tal situação é conhecida como laranjeira",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_dois = forms.ChoiceField(
        label="O senhor sabe falar algum outro idioma, além do português?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_tres = forms.CharField(
        label="Caso incorporado, quais são as expectativas do senhor para o serviço militar?")

    pergunta_quatro = forms.ChoiceField(
        label="O senhor possui algum parente que seja militar?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    pergunta_cinco = forms.ChoiceField(
        label="O senhor possui alguma habilidade profissional, curso técnico ou área de interesse?",
        widget=forms.RadioSelect, choices=LISTA_RESPOSTA_SN)

    class Meta:
        model = Questionariotres
        fields = ['pergunta_um', 'pergunta_dois', 'pergunta_tres',
                  'pergunta_quatro', 'pergunta_cinco']

