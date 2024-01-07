from django.shortcuts import redirect
from .models import Quartel
from subunidades.models import Subunidade
from viaturas.models import Armamento
from pessoas.models import Pessoa
from contatos.models import Contato
from enderecos.models import Endereco
from documentos.models import Documento
from militares.models import Militar, Atributos
import pandas as pd


def create_dados(request):
    unidade = request.user.pessoas.militar.unidade.id
    quartel = Quartel.objects.get(id=unidade)
    dataframe = pd.read_csv('media/uploads/2gac.csv', sep=';', encoding='latin1', engine='python')
    d_records = dataframe.to_dict("records")
    list_pessoas = []
    list_contatos = []
    list_enderecos = []
    list_documentos = []
    list_militares = []
    list_atributos = []
    for dado in d_records:
        p = Pessoa(nome_completo=dado['NOME'], data_nasc=dado['DT_NASCIMENTO'], situacao='Ativo')
        list_pessoas.append(p)
    Pessoa.objects.bulk_create(list_pessoas)
    for dado in d_records:
        pessoa = Pessoa.objects.get(nome_completo=dado['NOME'])
        c = Contato(email=dado['EMAIL_PESSOAL'].strip(), celular=dado['FONE_CELULAR'],
                    telefone=dado['FONE_RESIDENCIAL'], pessoa=pessoa)
        e = Endereco(logadouro=dado['Logadouro'], complemento=dado['Complemento'],
                     bairro=dado['Bairros'], cep=dado['CEP'],
                     cidade=dado['Cidade'], pessoa=pessoa)
        d = Documento(rg=dado['IDTCIVIL'], cpf=dado['CPF'], titulo_eleitor=dado['Titulo'],
                      zona_eleitoral=dado['Zona'], secao_eleitoral=dado['Secao'],
                      cnh=dado['Nr CNH'], cat_cnh=dado['CNH_CAT'], pessoa=pessoa)
        m = Militar(nome_guerra=dado['NOME_GUERRA'], identidade=dado['IDENTIDADE'],
                    data_praca=dado['DT_PRACA'], unidade=quartel, pessoa=pessoa,
                    posto_grad=dado['PGRAD'].strip())
        a = Atributos(militar=m)
        list_contatos.append(c)
        list_enderecos.append(e)
        list_documentos.append(d)
        list_militares.append(m)
        list_atributos.append(a)
    Contato.objects.bulk_create(list_contatos)
    Endereco.objects.bulk_create(list_enderecos)
    Documento.objects.bulk_create(list_documentos)
    Militar.objects.bulk_create(list_militares)
    Atributos.objects.bulk_create(list_atributos)
    return redirect('homepage')


def create_armt(request):
    unidade = request.user.pessoas.militar.unidade.id
    quartel = Quartel.objects.get(id=unidade)
    bc = Subunidade.objects.get(nome="Bateria Comando")
    pbia = Subunidade.objects.get(nome="1ª Bateria de Obuses")
    sbia = Subunidade.objects.get(nome="2ª Bateria de Obuses")
    dataframebc = pd.read_csv('media/uploads/bc_armt.csv', sep=';', encoding='latin1', engine='python')
    dataframepbia = pd.read_csv('media/uploads/1bia_armt.csv', sep=';', encoding='latin1', engine='python')
    dataframesbia = pd.read_csv('media/uploads/2bia_armt.csv', sep=';', encoding='latin1', engine='python')
    bc_records = dataframebc.to_dict("records")
    pbia_records = dataframepbia.to_dict("records")
    sbia_records = dataframesbia.to_dict("records")
    list_armt_bc = []
    list_armt_pbia = []
    list_armt_sbia = []
    for dado in bc_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      unidade=quartel, subunidade=bc)
        list_armt_bc.append(a)
    Armamento.objects.bulk_create(list_armt_bc)
    for dado in pbia_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      unidade=quartel, subunidade=pbia)
        list_armt_pbia.append(a)
    Armamento.objects.bulk_create(list_armt_pbia)
    for dado in sbia_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      unidade=quartel, subunidade=sbia)
        list_armt_sbia.append(a)
    Armamento.objects.bulk_create(list_armt_sbia)
    return redirect('homepage')

