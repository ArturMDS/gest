from militares.models import Observacao


lista_transgre = ['1. Faltar à verdade ou omitir deliberadamente informações que possam conduzir à apuração de uma '
                  'transgressão disciplinar', '2. Utilizar-se do anonimato',
                  '3. Concorrer para a discórdia ou a desarmonia ou cultivar inimizade entre militares ou seus '
                  'familiares', '4. Deixar de exercer autoridade compatível com seu posto ou graduação',
                  '5. Deixar de punir o subordinado que cometer transgressão, salvo na ocorrência das circunstâncias '
                  'de justificação previstas neste Regulamento',
                  '6. Não levar falta ou irregularidade que presenciar, ou de que tiver ciência e não lhe couber '
                  'reprimir, ao conhecimento de autoridade competente, no mais curto prazo',
                  '7. Retardar o cumprimento, deixar de cumprir ou de fazer cumprir norma regulamentar na esfera de '
                  'suas atribuições.',
                  '8. Deixar de comunicar a tempo, ao superior imediato, ocorrência no âmbito de suas atribuições, '
                  'quando se julgar suspeito ou impedido de providenciar a respeito',
                  '9. Deixar de cumprir prescrições expressamente estabelecidas no Estatuto dos Militares ou em '
                  'outras leis e regulamentos, desde que não haja tipificação como crime ou contravenção penal, '
                  'cuja violação afete os preceitos da hierarquia e disciplina, a ética militar, a honra pessoal, '
                  'o pundonor militar ou o decoro da classe',
                  '10. Deixar de instruir, na esfera de suas atribuições, processo que lhe for encaminhado, ressalvado '
                  'o caso em que não for possível obter elementos para tal',
                  '11. Deixar de encaminhar à autoridade competente, na linha de subordinação e no mais curto prazo, '
                  'recurso ou documento que receber elaborado de acordo com os preceitos regulamentares, se não for '
                  'da sua alçada a solução',
                  '12. Desrespeitar, retardar ou prejudicar medidas de cumprimento ou ações de ordem judicial, '
                  'administrativa ou policial, ou para isso concorrer',
                  '13. Apresentar parte ou recurso suprimindo instância administrativa, dirigindo para autoridade '
                  'incompetente, repetindo requerimento já rejeitado pela mesma autoridade ou empregando termos '
                  'desrespeitosos', '14. Dificultar ao subordinado a apresentação de recurso',
                  '15. Deixar de comunicar, tão logo possível, ao superior a execução de ordem recebida',
                  '16. Aconselhar ou concorrer para que não seja cumprida qualquer ordem de autoridade competente, '
                  'ou para retardar a sua execução',
                  '17. Deixar de cumprir ou alterar, sem justo motivo, as determinações constantes da missão recebida, '
                  'ou qualquer outra determinação escrita ou verbal',
                  '18. Simular doença para esquivar-se do cumprimento de qualquer dever militar',
                  '19. Trabalhar mal, intencionalmente ou por falta de atenção, em qualquer serviço ou instrução',
                  '20. Causar ou contribuir para a ocorrência de acidentes no serviço ou na instrução, por imperícia, '
                  'imprudência ou negligência', '21. Disparar arma por imprudência ou negligência',
                  '22. Não zelar devidamente, danificar ou extraviar por negligência ou desobediência das regras e '
                  'normas de serviço, material ou animal da União ou documentos oficiais, que estejam ou não sob sua '
                  'responsabilidade direta, ou concorrer para tal',
                  '23. Não ter pelo preparo próprio, ou pelo de seus comandados, instruendos ou educandos, a dedicação '
                  'imposta pelo sentimento do dever',
                  '24. Deixar de providenciar a tempo, na esfera de suas atribuições, por negligência, medidas contra '
                  'qualquer irregularidade de que venha a tomar conhecimento',
                  '25. Deixar de participar em tempo, à autoridade imediatamente superior, a impossibilidade de '
                  'comparecer à OM ou a qualquer ato de serviço para o qual tenha sido escalado ou a que deva '
                  'assistir',
                  '26. Faltar ou chegar atrasado, sem justo motivo, a qualquer ato, serviço ou instrução de que deva '
                  'participar ou a que deva assistir',
                  '27. Permutar serviço sem permissão de autoridade competente ou com o objetivo de obtenção de '
                  'vantagem pecuniária',
                  '28. Ausentar-se, sem a devida autorização, da sede da organização militar onde serve, do local do '
                  'serviço ou de outro qualquer em que deva encontrar-se por força de disposição legal ou ordem',
                  '29. Deixar de apresentar-se, nos prazos regulamentares, à OM para a qual tenha sido transferido ou '
                  'classificado e às autoridades competentes, nos casos de comissão ou serviço extraordinário para os '
                  'quais tenha sido designado',
                  '30. Não se apresentar ao fim de qualquer afastamento do serviço ou, ainda, logo que souber da '
                  'interrupção',
                  '31. Representar a organização militar ou a corporação, em qualquer ato, sem estar devidamente '
                  'autorizado',
                  '32. Assumir compromissos, prestar declarações ou divulgar informações, em nome da corporação ou da '
                  'unidade que comanda ou em que serve, sem autorização',
                  '33. Contrair dívida ou assumir compromisso superior às suas possibilidades, que afete o bom nome da '
                  'Instituição',
                  '34. Esquivar-se de satisfazer compromissos de ordem moral ou pecuniária que houver assumido, '
                  'afetando o bom nome da Instituição',
                  '35. Não atender, sem justo motivo, à observação de autoridade superior no sentido de satisfazer '
                  'débito já reclamado',
                  '36. Não atender à obrigação de dar assistência à sua família ou dependente legalmente constituídos, '
                  'de que trata o Estatuto dos Militares',
                  '37. Fazer diretamente, ou por intermédio de outrem, transações pecuniárias envolvendo assunto de '
                  'serviço, bens da União ou material cuja comercialização seja proibida',
                  '38. Realizar ou propor empréstimo de dinheiro a outro militar visando auferir lucro',
                  '39. Ter pouco cuidado com a apresentação pessoal ou com o asseio próprio ou coletivo',
                  '40. Portar-se de maneira inconveniente ou sem compostura',
                  '41. Deixar de tomar providências cabíveis, com relação ao procedimento de seus dependentes, '
                  'estabelecidos no Estatuto dos Militares, junto à sociedade, após devidamente admoestado por seu '
                  'Comandante',
                  '42. Freqüentar lugares incompatíveis com o decoro da sociedade ou da classe',
                  '43. Portar a praça armamento militar sem estar de serviço ou sem autorização',
                  '44. Executar toques de clarim ou corneta, realizar tiros de salva, fazer sinais regulamentares, '
                  'içar ou arriar a Bandeira Nacional ou insígnias, sem ordem para tal',
                  '45. Conversar ou fazer ruídos em ocasiões ou lugares impróprios quando em serviço ou em local sob '
                  'administração militar',
                  '46. Disseminar boatos no interior de OM ou concorrer para tal',
                  '47. Provocar ou fazer-se causa, voluntariamente, de alarme injustificável',
                  '48. Usar de força desnecessária no ato de efetuar prisão disciplinar ou de conduzir transgressor',
                  '49. Deixar alguém conversar ou entender-se com preso disciplinar, sem autorização de autoridade '
                  'competente',
                  '50. Conversar com sentinela, vigia, plantão ou preso disciplinar, sem para isso estar autorizado '
                  'por sua função ou por autoridade competente',
                  '51. Consentir que preso disciplinar conserve em seu poder instrumentos ou objetos não permitidos',
                  '52. Conversar, distrair-se, sentar-se ou fumar, quando exercendo função de sentinela, vigia ou '
                  'plantão da hora',
                  '53. Consentir, quando de sentinela, vigia ou plantão da hora, a formação de grupo ou a permanência '
                  'de pessoa junto a seu posto',
                  '54. Fumar em lugar ou ocasião onde seja vedado',
                  '55. Tomar parte em jogos proibidos ou em jogos a dinheiro, em área militar ou sob jurisdição '
                  'militar',
                  '56. Tomar parte, em área militar ou sob jurisdição militar, em discussão a respeito de assuntos de '
                  'natureza político-partidária ou religiosa',
                  '57. Manifestar-se, publicamente, o militar da ativa, sem que esteja autorizado, a respeito de '
                  'assuntos de natureza político-partidária',
                  '58. Tomar parte, fardado, em manifestações de natureza político-partidária',
                  '59. Discutir ou provocar discussão, por qualquer veículo de comunicação, sobre assuntos políticos '
                  'ou militares, exceto se devidamente autorizado',
                  '60. Ser indiscreto em relação a assuntos de caráter oficial cuja divulgação possa ser prejudicial à '
                  'disciplina ou à boa ordem do serviço',
                  '61. Dar conhecimento de atos, documentos, dados ou assuntos militares a quem deles não deva ter '
                  'ciência ou não tenha atribuições para neles intervir',
                  '62. Publicar ou contribuir para que sejam publicados documentos, fatos ou assuntos militares que '
                  'possam concorrer para o desprestígio das Forças Armadas ou que firam a disciplina ou a segurança '
                  'destas',
                  '63. Comparecer o militar da ativa, a qualquer atividade, em traje ou uniforme diferente do '
                  'determinado',
                  '64. Deixar o superior de determinar a saída imediata de solenidade militar ou civil, de subordinado '
                  'que a ela compareça em traje ou uniforme diferente do determinado',
                  '65. Apresentar-se, em qualquer situação, sem uniforme, mal uniformizado, com o uniforme alterado ou '
                  'em trajes em desacordo com as disposições em vigor',
                  '66. Sobrepor ao uniforme insígnia ou medalha não regulamentar, bem como, indevidamente, distintivo '
                  'ou condecoração',
                  '67. Recusar ou devolver insígnia, medalha ou condecoração que lhe tenha sido outorgada',
                  '68. Usar o militar da ativa, em via pública, uniforme inadequado, contrariando o Regulamento de '
                  'Uniformes do Exército ou normas a respeito',
                  '69. Transitar o soldado, o cabo ou o taifeiro, pelas ruas ou logradouros públicos, durante o '
                  'expediente, sem permissão da autoridade competente',
                  '70. Entrar ou sair da OM, ou ainda permanecer no seu interior o cabo ou soldado usando traje civil, '
                  'sem a devida permissão da autoridade competente',
                  '71. Entrar em qualquer OM, ou dela sair, o militar, por lugar que não seja para isso designado',
                  '72. Entrar em qualquer OM, ou dela sair, o taifeiro, o cabo ou o soldado, com objeto ou embrulho, '
                  'sem autorização do comandante da guarda ou de autoridade equivalente',
                  '73. Deixar o oficial ou aspirante-a-oficial, ao entrar em OM onde não sirva, de dar ciência da sua '
                  'presença ao oficial-de-dia e, em seguida, de procurar o comandante ou o oficial de maior '
                  'precedência hierárquica, para cumprimentá-lo',
                  '74. Deixar o subtenente, sargento, taifeiro, cabo ou soldado, ao entrar em organização militar onde '
                  'não sirva, de apresentar-se ao oficial-de-dia ou a seu substituto legal',
                  '75. Deixar o comandante da guarda ou responsável pela segurança correspondente, de cumprir as '
                  'prescrições regulamentares com respeito à entrada ou permanência na OM de civis ou militares a ela '
                  'estranhos',
                  '76. Adentrar o militar, sem permissão ou ordem, em aposentos destinados a superior ou onde este se '
                  'ache, bem como em qualquer lugar onde a entrada lhe seja vedada',
                  '77. Adentrar ou tentar entrar em alojamento de outra subunidade, depois da revista do recolher, '
                  'salvo os oficiais ou sargentos que, por suas funções, sejam a isso obrigados',
                  '78. Entrar ou permanecer em dependência da OM onde sua presença não seja permitida',
                  '79. Entrar ou sair de OM com tropa, sem prévio conhecimento, autorização ou ordem da autoridade '
                  'competente',
                  '80. Retirar ou tentar retirar de qualquer lugar sob jurisdição militar, material, viatura, '
                  'aeronave, embarcação ou animal, ou mesmo deles servir-se, sem ordem do responsável ou '
                  'proprietário',
                  '81. Abrir ou tentar abrir qualquer dependência de organização militar, fora das horas de '
                  'expediente, desde que não seja o respectivo chefe ou sem a devida ordem e a expressa declaração de '
                  'motivo, salvo em situações de emergência',
                  '82. Desrespeitar regras de trânsito, medidas gerais de ordem policial, judicial ou administrativa',
                  '83. Deixar de portar a identidade militar, estando ou não fardado',
                  '84. Deixar de se identificar quando solicitado por militar das Forças Armadas em serviço ou em '
                  'cumprimento de missão', '85. Desrespeitar, em público, as convenções sociais',
                  '86. Desconsiderar ou desrespeitar autoridade constituída',
                  '87. Desrespeitar corporação judiciária militar ou qualquer de seus membros',
                  '88. Faltar, por ação ou omissão, com o respeito devido aos símbolos nacionais, estaduais, '
                  'municipais e militares',
                  '89. Apresentar-se a superior hierárquico ou retirar-se de sua presença, sem obediência às normas '
                  'regulamentares',
                  '90. Deixar, quando estiver sentado, de demonstrar respeito, consideração e cordialidade ao superior '
                  'hierárquico, deixando de oferecer-lhe seu lugar, ressalvadas as situações em que houver lugar '
                  'marcado ou em que as convenções sociais assim não o indiquem',
                  '91. Sentar-se, sem a devida autorização, à mesa em que estiver superior hierárquico',
                  '92. Deixar, deliberadamente, de corresponder a cumprimento de subordinado',
                  '93. Deixar, deliberadamente, de cumprimentar superior hierárquico, uniformizado ou não, neste '
                  'último caso desde que o conheça, ou de saudá-lo de acordo com as normas regulamentares',
                  '94. Deixar o oficial ou aspirante-a-oficial, diariamente, tão logo seus afazeres o permitam, de '
                  'apresentar-se ao comandante ou ao substituto legal imediato da OM onde serve, para cumprimentá-lo, '
                  'salvo ordem ou outras normas em contrário',
                  '95. Deixar o subtenente ou sargento, diariamente, tão logo seus afazeres o permitam, de '
                  'apresentar-se ao seu comandante de subunidade ou chefe imediato, salvo ordem ou outras normas em '
                  'contrário',
                  '96. Recusar-se a receber vencimento, alimentação, fardamento, equipamento ou material que lhe seja '
                  'destinado ou deva ficar em seu poder ou sob sua responsabilidade',
                  '97. Recusar-se a receber equipamento, material ou documento que tenha solicitado oficialmente, para '
                  'atender a interesse próprio',
                  '98. Desacreditar, dirigir-se, referir-se ou responder de maneira desatenciosa a superior '
                  'hierárquico',
                  '99. Censurar ato de superior hierárquico ou procurar desconsiderá-lo seja entre militares, seja '
                  'entre civis',
                  '100. Ofender, provocar, desafiar, desconsiderar ou procurar desacreditar outro militar, por atos, '
                  'gestos ou palavras, mesmo entre civis.',
                  '101. Ofender a moral, os costumes ou as instituições nacionais ou do país estrangeiro em que se '
                  'encontrar, por atos, gestos ou palavras',
                  '102. Promover ou envolver-se em rixa, inclusive luta corporal, com outro militar',
                  '103. Autorizar, promover ou tomar parte em qualquer manifestação coletiva, seja de caráter '
                  'reivindicatório ou político, seja de crítica ou de apoio a ato de superior hierárquico, com exceção '
                  'das demonstrações íntimas de boa e sã camaradagem e com consentimento do homenageado',
                  '104. Aceitar qualquer manifestação coletiva de seus subordinados, com exceção das demonstrações '
                  'íntimas de boa e sã camaradagem e com consentimento do homenageado',
                  '105. Autorizar, promover, assinar representações, documentos coletivos ou publicações de qualquer '
                  'tipo, com finalidade política, de reivindicação coletiva ou de crítica a autoridades constituídas '
                  'ou às suas atividades',
                  '106. Autorizar, promover ou assinar petição ou memorial, de qualquer natureza, dirigido a '
                  'autoridade civil, sobre assunto da alçada da administração do Exército',
                  '107. Ter em seu poder, introduzir ou distribuir, em área militar ou sob a jurisdição militar, '
                  'publicações, estampas, filmes ou meios eletrônicos que atentem contra a disciplina ou a moral',
                  '108. Ter em seu poder ou introduzir, em área militar ou sob a jurisdição militar, armas, '
                  'explosivos, material inflamável, substâncias ou instrumentos proibidos, sem conhecimento ou '
                  'permissão da autoridade competente',
                  '109. Fazer uso, ter em seu poder ou introduzir, em área militar ou sob jurisdição militar, bebida '
                  'alcoólica ou com efeitos entorpecentes, salvo quando devidamente autorizado',
                  '110. Comparecer a qualquer ato de serviço em estado visível de embriaguez ou nele se embriagar',
                  '111. Falar, habitualmente, língua estrangeira em OM ou em área de estacionamento de tropa, exceto '
                  'quando o cargo ocupado o exigir',
                  '112. Exercer a praça, quando na ativa, qualquer atividade comercial ou industrial, ressalvadas as '
                  'permitidas pelo Estatuto dos Militares',
                  '113. Induzir ou concorrer intencionalmente para que outrem incida em transgressão disciplinar.']


def define_pontos(id_obs):
    observacao = Observacao.objects.get(id=id_obs)
    if observacao.tipo == 'negativa' and observacao.solucao == 'Advertência de Caráter Reservado':
        observacao.pontos = int(-2)
    elif observacao.tipo == 'negativa' and observacao.solucao == 'Advertência de Caráter Ostensivo':
        observacao.pontos = int(-3)
    elif observacao.tipo == 'negativa' and observacao.solucao == 'Impedimento Disciplinar':
        observacao.pontos = int(-4)
    elif observacao.tipo == 'negativa' and observacao.solucao == 'Repreensão':
        observacao.pontos = int(-5)
    elif observacao.tipo == 'negativa' and observacao.solucao == 'Detenção':
        observacao.pontos = int(-7)
    elif observacao.tipo == 'negativa' and observacao.solucao == 'Prisão':
        observacao.pontos = int(-10)
    elif observacao.tipo == 'positiva' and observacao.solucao == 'Dispensa Parcial do Serviço':
        observacao.pontos = 2
    elif observacao.tipo == 'positiva' and observacao.solucao == 'Dispensa Total do Serviço':
        observacao.pontos = 3
    elif observacao.tipo == 'positiva' and observacao.solucao == 'Referência Elogiosa':
        observacao.pontos = 5
    elif observacao.tipo == 'positiva' and observacao.solucao == 'Elogio':
        observacao.pontos = 10
    elif observacao.tipo == 'neutra':
        observacao.pontos = int(-1)
    observacao.save()


def define_atributos(id_obs, asks):
    observacao = Observacao.objects.get(id=id_obs)
    if 'camaradagem' in asks:
        observacao.arrolado.atributos.camaradagem += observacao.pontos
        observacao.is_used = True
    if 'iniciativa' in asks:
        observacao.arrolado.atributos.iniciativa += observacao.pontos
        observacao.is_used = True
    if 'persistencia' in asks:
        observacao.arrolado.atributos.persistencia += observacao.pontos
        observacao.is_used = True
    if 'responsabilidade' in asks:
        observacao.arrolado.atributos.responsabilidade += observacao.pontos
        observacao.is_used = True
    if 'coragem' in asks:
        observacao.arrolado.atributos.coragem += observacao.pontos
        observacao.is_used = True
    if 'disciplina' in asks:
        observacao.arrolado.atributos.disciplina += observacao.pontos
        observacao.is_used = True
    if 'apresentacao' in asks:
        observacao.arrolado.atributos.apresentacao += observacao.pontos
        observacao.is_used = True
    if 'dedicacao' in asks:
        observacao.arrolado.atributos.dedicacao += observacao.pontos
        observacao.is_used = True
    if 'resistencia_fisica' in asks:
        observacao.arrolado.atributos.resistencia_fisica += observacao.pontos
        observacao.is_used = True
    if 'conhecimento_tecnico' in asks:
        observacao.arrolado.atributos.conhecimento_tecnico += observacao.pontos
        observacao.is_used = True
    observacao.save()
    observacao.arrolado.atributos.save()

