from django.db import models
from django.utils import timezone
from pessoas.models import Pessoa
from subunidades.models import Subunidade
from quarteis.models import Quartel

LISTA_PG = (
    ("General de Exército", "Gen Ex"),
    ("General de Divisão", "Gen Div"),
    ("General de Brigada", "Gen Bda"),
    ("Coronel", "Cel"),
    ("Tenente Coronel", "Ten Cel"),
    ("Major", "Maj"),
    ("Capitão", "Cap"),
    ("1º Tenente", "1º Ten"),
    ("2º Tenente", "2º Ten"),
    ("Aspirante à Oficial", "Asp Of"),
    ("Subtenente", "ST"),
    ("1º Sargento", "1º Sgt"),
    ("2º Sargento", "2º Sgt"),
    ("3º Sargento", "3º Sgt"),
    ("Cabo", "Cabo"),
    ("Solcado NB", "Sd NB"),
    ("Soldado EV", "Sd EV"),
    ("Conscrito", "Conscrito")
)

LISTA_TIPO = (
    ("positiva", "FO+"),
    ("negativa", "FO-"),
    ("neutra", "N")
)

LISTA_SOL = (
    ("Sem solução", "Sem solução"),
    ("Justificado", "Justificado"),
    ("Advertência de Caráter Reservado", "ACR"),
    ("Advertência de Caráter Ostensivo", "ACO"),
    ("Impedimento Disciplinar", "ID"),
    ("Repreensão", "Rep"),
    ("Detenção", "Det"),
    ("Prisão", "Prisão"),
    ("Elogio", "Elogio"),
    ("Referência Elogiosa", "Referência Elogiosa"),
    ("Dispensa Total do Serviço", "Dispensa Total do Serviço"),
    ("Dispensa Parcial do Serviço", "Dispensa Parcial do Serviço"),
)

LISTA_TRANSG = (
    ("Sem amparo", "Sem amparo"),
    ("1. Faltar à verdade ou omitir deliberadamente informações que possam conduzir à apuração de uma "
     "transgressão disciplinar", "1"),
    ("2. Utilizar-se do anonimato", "2"),
    ("3. Concorrer para a discórdia ou a desarmonia ou cultivar inimizade entre militares ou seus familiares", "3"),
    ("4. Deixar de exercer autoridade compatível com seu posto ou graduação", "4"),
    ("5. Deixar de punir o subordinado que cometer transgressão, salvo na ocorrência das circunstâncias de "
     "justificação previstas neste Regulamento", "5"),
    ("6. Não levar falta ou irregularidade que presenciar, ou de que tiver ciência e não lhe couber reprimir, "
     "ao conhecimento de autoridade competente, no mais curto prazo", "6"),
    ("7. Retardar o cumprimento, deixar de cumprir ou de fazer cumprir norma regulamentar na esfera de suas "
     "atribuições.", "7"),
    ("8. Deixar de comunicar a tempo, ao superior imediato, ocorrência no âmbito de suas atribuições, "
     "quando se julgar suspeito ou impedido de providenciar a respeito", "8"),
    ("9. Deixar de cumprir prescrições expressamente estabelecidas no Estatuto dos Militares ou em outras "
     "leis e regulamentos, desde que não haja tipificação como crime ou contravenção penal, cuja violação "
     "afete os preceitos da hierarquia e disciplina, a ética militar, a honra pessoal, o pundonor militar "
     "ou o decoro da classe", "9"),
    ("10. Deixar de instruir, na esfera de suas atribuições, processo que lhe for encaminhado, "
     "ressalvado o caso em que não for possível obter elementos para tal", "10"),
    ("11. Deixar de encaminhar à autoridade competente, na linha de subordinação e no mais curto prazo, "
     "recurso ou documento que receber elaborado de acordo com os preceitos regulamentares, se não for da sua "
     "alçada a solução", "11"),
    ("12. Desrespeitar, retardar ou prejudicar medidas de cumprimento ou ações de ordem judicial, "
     "administrativa ou policial, ou para isso concorrer", "12"),
    ("13. Apresentar parte ou recurso suprimindo instância administrativa, dirigindo para autoridade incompetente, "
     "repetindo requerimento já rejeitado pela mesma autoridade ou empregando termos desrespeitosos", "13"),
    ("14. Dificultar ao subordinado a apresentação de recurso", "14"),
    ("15. Deixar de comunicar, tão logo possível, ao superior a execução de ordem recebida", "15"),
    ("16. Aconselhar ou concorrer para que não seja cumprida qualquer ordem de autoridade competente, "
     "ou para retardar a sua execução", "16"),
    ("17. Deixar de cumprir ou alterar, sem justo motivo, as determinações constantes da missão recebida, "
     "ou qualquer outra determinação escrita ou verbal", "17"),
    ("18. Simular doença para esquivar-se do cumprimento de qualquer dever militar", "18"),
    ("19. Trabalhar mal, intencionalmente ou por falta de atenção, em qualquer serviço ou instrução", "19"),
    ("20. Causar ou contribuir para a ocorrência de acidentes no serviço ou na instrução, por imperícia, "
     "imprudência ou negligência", "20"),
    ("21. Disparar arma por imprudência ou negligência", "21"),
    ("22. Não zelar devidamente, danificar ou extraviar por negligência ou desobediência das regras e "
     "normas de serviço, material ou animal da União ou documentos oficiais, que estejam ou não sob sua "
     "responsabilidade direta, ou concorrer para tal", "22"),
    ("23. Não ter pelo preparo próprio, ou pelo de seus comandados, instruendos ou educandos, a dedicação imposta "
     "pelo sentimento do dever", "23"),
    ("24. Deixar de providenciar a tempo, na esfera de suas atribuições, por negligência, medidas contra qualquer "
     "irregularidade de que venha a tomar conhecimento", "24"),
    ("25. Deixar de participar em tempo, à autoridade imediatamente superior, a impossibilidade de comparecer à OM "
     "ou a qualquer ato de serviço para o qual tenha sido escalado ou a que deva assistir", "25"),
    ("26. Faltar ou chegar atrasado, sem justo motivo, a qualquer ato, serviço ou instrução de que deva participar "
     "ou a que deva assistir", "26"),
    ("27. Permutar serviço sem permissão de autoridade competente ou com o objetivo de obtenção de vantagem pecuniária",
     "27"),
    ("28. Ausentar-se, sem a devida autorização, da sede da organização militar onde serve, do local do serviço ou de "
     "outro qualquer em que deva encontrar-se por força de disposição legal ou ordem", "28"),
    ("29. Deixar de apresentar-se, nos prazos regulamentares, à OM para a qual tenha sido transferido ou classificado "
     "e às autoridades competentes, nos casos de comissão ou serviço extraordinário para os quais tenha sido designado",
     "29"),
    ("30. Não se apresentar ao fim de qualquer afastamento do serviço ou, ainda, logo que souber da interrupção", "30"),
    ("31. Representar a organização militar ou a corporação, em qualquer ato, sem estar devidamente autorizado", "31"),
    ("32. Assumir compromissos, prestar declarações ou divulgar informações, em nome da corporação ou da unidade que "
     "comanda ou em que serve, sem autorização", "32"),
    ("33. Contrair dívida ou assumir compromisso superior às suas possibilidades, que afete o bom nome da Instituição",
     "33"),
    ("34. Esquivar-se de satisfazer compromissos de ordem moral ou pecuniária que houver assumido, afetando o bom nome "
     "da Instituição", "34"),
    ("35. Não atender, sem justo motivo, à observação de autoridade superior no sentido de satisfazer débito já "
     "reclamado", "35"),
    ("36. Não atender à obrigação de dar assistência à sua família ou dependente legalmente constituídos, "
     "de que trata o Estatuto dos Militares", "36"),
    ("37. Fazer diretamente, ou por intermédio de outrem, transações pecuniárias envolvendo assunto de serviço, "
     "bens da União ou material cuja comercialização seja proibida", "37"),
    ("38. Realizar ou propor empréstimo de dinheiro a outro militar visando auferir lucro", "38"),
    ("39. Ter pouco cuidado com a apresentação pessoal ou com o asseio próprio ou coletivo", "39"),
    ("40. Portar-se de maneira inconveniente ou sem compostura", "40"),
    ("41. Deixar de tomar providências cabíveis, com relação ao procedimento de seus dependentes, estabelecidos no "
     "Estatuto dos Militares, junto à sociedade, após devidamente admoestado por seu Comandante", "41"),
    ("42. Frequentar lugares incompatíveis com o decoro da sociedade ou da classe", "42"),
    ("43. Portar a praça armamento militar sem estar de serviço ou sem autorização", "43"),
    ("44. Executar toques de clarim ou corneta, realizar tiros de salva, fazer sinais regulamentares, içar ou arriar a "
     "Bandeira Nacional ou insígnias, sem ordem para tal", "44"),
    ("45. Conversar ou fazer ruídos em ocasiões ou lugares impróprios quando em serviço ou em local sob administração "
     "militar", "45"),
    ("46. Disseminar boatos no interior de OM ou concorrer para tal", "46"),
    ("47. Provocar ou fazer-se causa, voluntariamente, de alarme injustificável", "47"),
    ("48. Usar de força desnecessária no ato de efetuar prisão disciplinar ou de conduzir transgressor", "48"),
    ("49. Deixar alguém conversar ou entender-se com preso disciplinar, sem autorização de autoridade competente",
     "49"),
    ("50. Conversar com sentinela, vigia, plantão ou preso disciplinar, sem para isso estar autorizado por sua função "
     "ou por autoridade competente", "50"),
    ("51. Consentir que preso disciplinar conserve em seu poder instrumentos ou objetos não permitidos", "51"),
    ("52. Conversar, distrair-se, sentar-se ou fumar, quando exercendo função de sentinela, vigia ou plantão da hora",
     "52"),
    ("53. Consentir, quando de sentinela, vigia ou plantão da hora, a formação de grupo ou a permanência de pessoa "
     "junto a seu posto", "53"),
    ("54. Fumar em lugar ou ocasião onde seja vedado", "54"),
    ("55. Tomar parte em jogos proibidos ou em jogos a dinheiro, em área militar ou sob jurisdição militar", "55"),
    ("56. Tomar parte, em área militar ou sob jurisdição militar, em discussão a respeito de assuntos de natureza "
     "político-partidária ou religiosa", "56"),
    ("57. Manifestar-se, publicamente, o militar da ativa, sem que esteja autorizado, a respeito de assuntos de "
     "natureza político-partidária", "57"),
    ("58. Tomar parte, fardado, em manifestações de natureza político-partidária", "58"),
    ("59. Discutir ou provocar discussão, por qualquer veículo de comunicação, sobre assuntos políticos ou militares, "
     "exceto se devidamente autorizado", "59"),
    ("60. Ser indiscreto em relação a assuntos de caráter oficial cuja divulgação possa ser prejudicial à disciplina "
     "ou à boa ordem do serviço", "60"),
    ("61. Dar conhecimento de atos, documentos, dados ou assuntos militares a quem deles não deva ter ciência ou não "
     "tenha atribuições para neles intervir", "61"),
    ("62. Publicar ou contribuir para que sejam publicados documentos, fatos ou assuntos militares que possam "
     "concorrer para o desprestígio das Forças Armadas ou que firam a disciplina ou a segurança destas", "62"),
    ("63. Comparecer o militar da ativa, a qualquer atividade, em traje ou uniforme diferente do determinado", "63"),
    ("64. Deixar o superior de determinar a saída imediata de solenidade militar ou civil, de subordinado que a ela "
     "compareça em traje ou uniforme diferente do determinado", "64"),
    ("65. Apresentar-se, em qualquer situação, sem uniforme, mal uniformizado, com o uniforme alterado ou em trajes em "
     "desacordo com as disposições em vigor", "65"),
    ("66. Sobrepor ao uniforme insígnia ou medalha não regulamentar, bem como, indevidamente, distintivo ou "
     "condecoração", "66"),
    ("67. Recusar ou devolver insígnia, medalha ou condecoração que lhe tenha sido outorgada", "67"),
    ("68. Usar o militar da ativa, em via pública, uniforme inadequado, contrariando o Regulamento de Uniformes do "
     "Exército ou normas a respeito", "68"),
    ("69. Transitar o soldado, o cabo ou o taifeiro, pelas ruas ou logradouros públicos, durante o expediente, "
     "sem permissão da autoridade competente", "69"),
    ("70. Entrar ou sair da OM, ou ainda permanecer no seu interior o cabo ou soldado usando traje civil, "
     "sem a devida permissão da autoridade competente", "70"),
    ("71. Entrar em qualquer OM, ou dela sair, o militar, por lugar que não seja para isso designado", "71"),
    ("72. Entrar em qualquer OM, ou dela sair, o taifeiro, o cabo ou o soldado, com objeto ou embrulho, "
     "sem autorização do comandante da guarda ou de autoridade equivalente", "72"),
    ("73. Deixar o oficial ou aspirante-a-oficial, ao entrar em OM onde não sirva, de dar ciência da sua presença ao "
     "oficial-de-dia e, em seguida, de procurar o comandante ou o oficial de maior precedência hierárquica, para "
     "cumprimentá-lo", "73"),
    ("74. Deixar o subtenente, sargento, taifeiro, cabo ou soldado, ao entrar em organização militar onde não sirva, "
     "de apresentar-se ao oficial-de-dia ou a seu substituto legal", "74"),
    ("75. Deixar o comandante da guarda ou responsável pela segurança correspondente, de cumprir as prescrições "
     "regulamentares com respeito à entrada ou permanência na OM de civis ou militares a ela estranhos", "75"),
    ("76. Adentrar o militar, sem permissão ou ordem, em aposentos destinados a superior ou onde este se ache, "
     "bem como em qualquer lugar onde a entrada lhe seja vedada", "76"),
    ("77. Adentrar ou tentar entrar em alojamento de outra subunidade, depois da revista do recolher, salvo os "
     "oficiais ou sargentos que, por suas funções, sejam a isso obrigados", "77"),
    ("78. Entrar ou permanecer em dependência da OM onde sua presença não seja permitida", "78"),
    ("79. Entrar ou sair de OM com tropa, sem prévio conhecimento, autorização ou ordem da autoridade competente",
     "79"),
    ("80. Retirar ou tentar retirar de qualquer lugar sob jurisdição militar, material, viatura, aeronave, embarcação "
     "ou animal, ou mesmo deles servir-se, sem ordem do responsável ou proprietário", "80"),
    ("81. Abrir ou tentar abrir qualquer dependência de organização militar, fora das horas de expediente, "
     "desde que não seja o respectivo chefe ou sem a devida ordem e a expressa declaração de motivo, "
     "salvo em situações de emergência", "81"),
    ("82. Desrespeitar regras de trânsito, medidas gerais de ordem policial, judicial ou administrativa", "82"),
    ("83. Deixar de portar a identidade militar, estando ou não fardado", "83"),
    ("84. Deixar de se identificar quando solicitado por militar das Forças Armadas em serviço ou em cumprimento de "
     "missão", "84"),
    ("85. Desrespeitar, em público, as convenções sociais", "85"),
    ("86. Desconsiderar ou desrespeitar autoridade constituída", "86"),
    ("87. Desrespeitar corporação judiciária militar ou qualquer de seus membros", "87"),
    ("88. Faltar, por ação ou omissão, com o respeito devido aos símbolos nacionais, estaduais, municipais e militares",
     "88"),
    ("89. Apresentar-se a superior hierárquico ou retirar-se de sua presença, sem obediência às normas regulamentares",
     "89"),
    ("90. Deixar, quando estiver sentado, de demonstrar respeito, consideração e cordialidade ao superior hierárquico, "
     "deixando de oferecer-lhe seu lugar, ressalvadas as situações em que houver lugar marcado ou em que as convenções "
     "sociais assim não o indiquem", "90"),
    ("91. Sentar-se, sem a devida autorização, à mesa em que estiver superior hierárquico", "91"),
    ("92. Deixar, deliberadamente, de corresponder a cumprimento de subordinado", "92"),
    ("93. Deixar, deliberadamente, de cumprimentar superior hierárquico, uniformizado ou não, neste último caso desde "
     "que o conheça, ou de saudá-lo de acordo com as normas regulamentares", "93"),
    ("94. Deixar o oficial ou aspirante-a-oficial, diariamente, tão logo seus afazeres o permitam, de apresentar-se "
     "ao comandante ou ao substituto legal imediato da OM onde serve, para cumprimentá-lo, salvo ordem ou outras "
     "normas em contrário", "94"),
    ("95. Deixar o subtenente ou sargento, diariamente, tão logo seus afazeres o permitam, de apresentar-se ao seu "
     "comandante de subunidade ou chefe imediato, salvo ordem ou outras normas em contrário", "95"),
    ("96. Recusar-se a receber vencimento, alimentação, fardamento, equipamento ou material que lhe seja destinado ou "
     "deva ficar em seu poder ou sob sua responsabilidade", "96"),
    ("97. Recusar-se a receber equipamento, material ou documento que tenha solicitado oficialmente, para atender a "
     "interesse próprio", "97"),
    ("98. Desacreditar, dirigir-se, referir-se ou responder de maneira desatenciosa a superior hierárquico", "98"),
    ("99. Censurar ato de superior hierárquico ou procurar desconsiderá-lo seja entre militares, seja entre civis",
     "99"),
    ("100. Ofender, provocar, desafiar, desconsiderar ou procurar desacreditar outro militar, por atos, gestos ou "
     "palavras, mesmo entre civis.", "100"),
    ("101. Ofender a moral, os costumes ou as instituições nacionais ou do país estrangeiro em que se encontrar, "
     "por atos, gestos ou palavras", "101"),
    ("102. Promover ou envolver-se em rixa, inclusive luta corporal, com outro militar", "102"),
    ("103. Autorizar, promover ou tomar parte em qualquer manifestação coletiva, seja de caráter reivindicatório ou "
     "político, seja de crítica ou de apoio a ato de superior hierárquico, com exceção das demonstrações íntimas de "
     "boa e sã camaradagem e com consentimento do homenageado", "103"),
    ("104. Aceitar qualquer manifestação coletiva de seus subordinados, com exceção das demonstrações íntimas de boa e "
     "sã camaradagem e com consentimento do homenageado", "104"),
    ("105. Autorizar, promover, assinar representações, documentos coletivos ou publicações de qualquer tipo, com "
     "finalidade política, de reivindicação coletiva ou de crítica a autoridades constituídas ou às suas atividades",
     "105"),
    ("106. Autorizar, promover ou assinar petição ou memorial, de qualquer natureza, dirigido a autoridade civil, "
     "sobre assunto da alçada da administração do Exército", "106"),
    ("107. Ter em seu poder, introduzir ou distribuir, em área militar ou sob a jurisdição militar, publicações, "
     "estampas, filmes ou meios eletrônicos que atentem contra a disciplina ou a moral", "107"),
    ("108. Ter em seu poder ou introduzir, em área militar ou sob a jurisdição militar, armas, explosivos, material "
     "inflamável, substâncias ou instrumentos proibidos, sem conhecimento ou permissão da autoridade competente",
     "108"),
    ("109. Fazer uso, ter em seu poder ou introduzir, em área militar ou sob jurisdição militar, bebida alcoólica ou "
     "com efeitos entorpecentes, salvo quando devidamente autorizado", "109"),
    ("110. Comparecer a qualquer ato de serviço em estado visível de embriaguez ou nele se embriagar", "110"),
    ("111. Falar, habitualmente, língua estrangeira em OM ou em área de estacionamento de tropa, exceto quando o "
     "cargo ocupado o exigir", "111"),
    ("112. Exercer a praça, quando na ativa, qualquer atividade comercial ou industrial, ressalvadas as permitidas "
     "pelo Estatuto dos Militares", "112"),
    ("113. Induzir ou concorrer intencionalmente para que outrem incida em transgressão disciplinar", "113"),
)


class Qualificacao(models.Model):
    qm = models.CharField(max_length=80)

    def __str__(self):
        return self.qm


class Militar(models.Model):
    nome_guerra = models.CharField(max_length=80)
    identidade = models.CharField(max_length=15, null=True, blank=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    data_praca = models.DateField(blank=True, null=True)
    subunidade = models.ForeignKey(Subunidade, related_name="mil_su", on_delete=models.PROTECT, null=True, blank=True)
    unidade = models.ForeignKey(Quartel, related_name="mil_om", on_delete=models.PROTECT)
    qualificacao = models.ForeignKey('Qualificacao', related_name="mil_qualif",
                                     on_delete=models.PROTECT, null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="militar", on_delete=models.CASCADE)
    posto_grad = models.CharField(
        max_length=30,
        choices=LISTA_PG,
        default="Soldado EV"
    )
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_guerra


class Atributos(models.Model):
    camaradagem = models.IntegerField(default=100)
    iniciativa = models.IntegerField(default=100)
    persistencia = models.IntegerField(default=100)
    responsabilidade = models.IntegerField(default=100)
    coragem = models.IntegerField(default=100)
    disciplina = models.IntegerField(default=100)
    apresentacao = models.IntegerField(default=100)
    dedicacao = models.IntegerField(default=100)
    resistencia_fisica = models.IntegerField(default=100)
    conhecimento_tecnico = models.IntegerField(default=100)
    ranking_inicial = models.IntegerField(default=0)
    militar = models.OneToOneField(Militar, related_name="atributos", on_delete=models.CASCADE)

    def __str__(self):
        return self.militar.nome_guerra


class Observacao(models.Model):
    tipo = models.CharField(
        max_length=10,
        choices=LISTA_TIPO,
        default="neutra",
    )
    relato_fato = models.TextField(max_length=500)
    arrolado = models.ForeignKey('Militar', related_name="mil_arrolado", on_delete=models.PROTECT)
    participante = models.ForeignKey('Militar', related_name="mil_part", on_delete=models.PROTECT)
    data = models.DateField(default=timezone.now)
    nr_processo = models.IntegerField(default=0)
    solucao = models.CharField(
        max_length=50,
        choices=LISTA_SOL,
        default="Sem solução",
    )
    enquadramento = models.CharField(
        max_length=500,
        choices=LISTA_TRANSG,
        default="Sem amparo",
    )
    dias = models.IntegerField(blank=True, null=True)
    publicacao_bi = models.CharField(max_length=200, blank=True, null=True)
    pontos = models.IntegerField(default=0)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.arrolado.nome_guerra


class Destino(models.Model):
    check_in = models.DateTimeField(auto_now=False, help_text='dd/mm/aaaa hh:mm:ss')
    check_out = models.DateTimeField(auto_now=False, help_text='dd/mm/aaaa hh:mm:ss', null=True, blank=True)
    motivo = models.CharField(max_length=200)
    in_force = models.BooleanField(default=True)
    militar = models.ForeignKey('Militar', related_name="destino", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.militar) + " - " + str(self.check_in)
