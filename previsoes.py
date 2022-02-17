#variação - NU_IDADE - 14 AO 71 / CN - 0 AO 791.9 / CH - 0 AO 753.30 / LC - 0 AO 733.10 / MT - 0 AO 951.80 / REDACAO - 0 AO 980 / Q005 - 1 AO 20

#1ª PREVISAO
previsao1 = pd.DataFrame({
    'TP_SEXO_M': 1, 
    'TP_COR_RACA_1': 1, 
    'TP_ESTADO_CIVIL_1': 1, 
    'SG_UF_RESIDENCIA_SP': 1, 
    'Q001_G': 1, 
    'Q002_G': 1,
    'Q006_Q': 1, 
    'NU_IDADE': 18,
    'NU_NOTA_CN': 700,
    'NU_NOTA_CH': 700,
    'NU_NOTA_LC': 700,
    'NU_NOTA_MT': 700,
    'NU_NOTA_REDACAO': 700,
    'Q005': 3,
    'NU_NOTA_MEDIA': 700})


values = 
    { 
'TP_SEXO_M': 0,
'TP_COR_RACA_1': 0, #Branca
'TP_COR_RACA_2': 0, #Preta
'TP_COR_RACA_3': 0, #Parda
'TP_COR_RACA_4': 0, #Amarela
'TP_COR_RACA_5': 0, #Indígena
'TP_ESTADO_CIVIL_1': 0, #Solteiro(a)
'TP_ESTADO_CIVIL_2': 0, #Casado(a)/Mora com companheiro(a)
'TP_ESTADO_CIVIL_3': 0, #Divorciado(a)/Desquitado(a)/Separado(a)
'TP_ESTADO_CIVIL_4': 0, #Viuvo(a)
'SG_UF_RESIDENCIA_AM': 0,
'SG_UF_RESIDENCIA_BA': 0,
'SG_UF_RESIDENCIA_CE': 0,
'SG_UF_RESIDENCIA_MT': 0,
'SG_UF_RESIDENCIA_RJ': 0,
'SG_UF_RESIDENCIA_RS': 0,
'SG_UF_RESIDENCIA_SC': 0,
'SG_UF_RESIDENCIA_SP': 0,
'Q001_B': 0, #Não completou a 4ª série/5º ano do Ensino Fundamental.
'Q001_C': 0, #Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
'Q001_D': 0, #Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
'Q001_E': 0, #Completou o Ensino Médio, mas não completou a Faculdade.
'Q001_F': 0, #Completou a Faculdade, mas não completou a Pós-graduação.
'Q001_G': 0, #Completou a Pós-graduação.
'Q001_H': 0, #Não sei.
'Q002_B': 0, #Não completou a 4ª série/5º ano do Ensino Fundamental.
'Q002_C': 0, #Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
'Q002_D': 0, #Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
'Q002_E': 0, #Completou o Ensino Médio, mas não completou a Faculdade.
'Q002_F': 0, #Completou a Faculdade, mas não completou a Pós-graduação.
'Q002_G': 0, #Completou a Pós-graduação.
'Q002_H': 0, #Não sei.
'Q003_B': 0,  
'Q003_C': 0,  
'Q003_D': 0,  
'Q003_E': 0,  
'Q003_F': 0,  
'Q004_B': 0, 
'Q004_C': 0, 
'Q004_D': 0, 
'Q004_E': 0, 
'Q004_F': 0, 
'Q006_B': 0, #Até R$ 998,00.
'Q006_H': 0, #De R$ 3.992,01 até R$ 4.990,00.
'Q006_N': 0, #De R$ 9.980,01 até R$ 11.976,00.
'Q006_Q': 0, #Mais de R$ 19.960,00.
'NU_IDADE': 0,
'NU_NOTA_CN': 0,
'NU_NOTA_CH': 0,
'NU_NOTA_LC': 0,
'NU_NOTA_MT': 0,
'NU_NOTA_REDACAO': 0,
'Q005': 0,
'NU_NOTA_MEDIA': 0

}

df = pd.DataFrame(values)





#Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.
#Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
#Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
#Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
#Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
#Não sei.


#Até R$ 998,00.
#De R$ 998,01 até R$ 1.497,00.
#De R$ 1.497,01 até R$ 1.996,00.
#De R$ 1.996,01 até R$ 2.495,00.
#De R$ 2.495,01 até R$ 2.994,00.
#De R$ 2.994,01 até R$ 3.992,00.
#De R$ 3.992,01 até R$ 4.990,00.
#De R$ 4.990,01 até R$ 5.988,00.
#De R$ 5.988,01 até R$ 6.986,00.
#De R$ 6.986,01 até R$ 7.984,00.
#De R$ 7.984,01 até R$ 8.982,00.
#De R$ 8.982,01 até R$ 9.980,00.
#De R$ 9.980,01 até R$ 11.976,00.
#De R$ 11.976,01 até R$ 14.970,00.
#De R$ 14.970,01 até R$ 19.960,00.
#Mais de R$ 19.960,00.


default_prevision = pd.DataFrame([
    {
'TP_SEXO_M': 0, 
'TP_COR_RACA_1': 0, 
'TP_COR_RACA_2': 0, 
'TP_COR_RACA_3': 0,
'TP_COR_RACA_4': 0, 
'TP_COR_RACA_5': 0, 
'TP_ESTADO_CIVIL_1': 0,
'TP_ESTADO_CIVIL_2': 0, 
'TP_ESTADO_CIVIL_3': 0, 
'TP_ESTADO_CIVIL_4': 0,
'SG_UF_RESIDENCIA_AL': 0, 
'SG_UF_RESIDENCIA_AM': 0, 
'SG_UF_RESIDENCIA_AP': 0,
'SG_UF_RESIDENCIA_BA': 0, 
'SG_UF_RESIDENCIA_CE': 0, 
'SG_UF_RESIDENCIA_DF': 0,
'SG_UF_RESIDENCIA_ES': 0, 
'SG_UF_RESIDENCIA_GO': 0, 
'SG_UF_RESIDENCIA_MA': 0,
'SG_UF_RESIDENCIA_MG': 0, 
'SG_UF_RESIDENCIA_MS': 0, 
'SG_UF_RESIDENCIA_MT': 0,
'SG_UF_RESIDENCIA_PA': 0, 
'SG_UF_RESIDENCIA_PB': 0, 
'SG_UF_RESIDENCIA_PE': 0,
'SG_UF_RESIDENCIA_PI': 0, 
'SG_UF_RESIDENCIA_PR': 0, 
'SG_UF_RESIDENCIA_RJ': 0,
'SG_UF_RESIDENCIA_RN': 0, 
'SG_UF_RESIDENCIA_RO': 0, 
'SG_UF_RESIDENCIA_RR': 0,
'SG_UF_RESIDENCIA_RS': 0, 
'SG_UF_RESIDENCIA_SC': 0, 
'SG_UF_RESIDENCIA_SE': 0,
'SG_UF_RESIDENCIA_SP': 0, 
'SG_UF_RESIDENCIA_TO': 0, 
'Q001_B': 0, 
'Q001_C': 0,
'Q001_D': 0, 
'Q001_E': 0, 
'Q001_F': 0, 
'Q001_G': 0, 
'Q001_H': 0, 
'Q002_B': 0, 
'Q002_C': 0,
'Q002_D': 0, 
'Q002_E': 0, 
'Q002_F': 0, 
'Q002_G': 0, 
'Q002_H': 0, 
'Q003_B': 0, 
'Q003_C': 0,
'Q003_D': 0, 
'Q003_E': 0, 
'Q003_F': 0, 
'Q004_B': 0, 
'Q004_C': 0, 
'Q004_D': 0, 
'Q004_E': 0,
'Q004_F': 0, 
'Q006_B': 0, 
'Q006_C': 0, 
'Q006_D': 0, 
'Q006_E': 0, 
'Q006_F': 0, 
'Q006_G': 0,
'Q006_H': 0, 
'Q006_I': 0, 
'Q006_J': 0, 
'Q006_K': 0, 
'Q006_L': 0, 
'Q006_M': 0, 
'Q006_N': 0,
'Q006_O': 0, 
'Q006_P': 0, 
'Q006_Q': 0, 
'NU_IDADE': 0, 
'NU_NOTA_CN': 0, 
'NU_NOTA_CH': 0,
'NU_NOTA_LC': 0, 
'NU_NOTA_MT': 0, 
'NU_NOTA_REDACAO': 0, 
'Q005': 0, 
'NU_NOTA_MEDIA': 0
]})