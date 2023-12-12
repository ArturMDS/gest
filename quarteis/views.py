from django.shortcuts import render, redirect
from .models import Quartel
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

