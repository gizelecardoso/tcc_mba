# Resultados Preliminares

## Extração

Resultados iniciais se concentram na base de dados do Enem do ano de 2019 disponibilizada pelo INEP, com mais de 5 milhões de observações. Para ajudar na manipulação desses dados, o primeiro passo foi a inserção no Banco de Dados MySQL, após isso foi realizada a coleta de uma amostra aleatória de 10000 observações, que de acordo com o Teorema do Limite Central, o resultado médio de uma amostra aleatória não se desviará do resultado médio da população de onde foi retirada essa amostra.

## Tratamento

Com os dados lidos, foi iniciada a fase de Tratamento para posterior inserção no Modelo de Machine Learning.

## Dados Ausentes:

Dados NaN (Not a Number), são os valores que não existem na base de dados, o motivo pode ser pelo não preenchimento desses dados, ou por falta dessa informação ou por uma coleta mal executada.

Figura 1. Dados Ausentes por Colunas do Dataset
Fonte: Resultados originais da pesquisa

As colunas apresentadas são fundamentais para a análise, e como a porcentagem de dados ausentes está abaixo de 30% opta-se por preencher esses dados com algum valor específico, no caso, a mediana será o valor escolhido para preenchimento dos dados ausentes. Já a variável TP_ENSINO (Tipo de instituição que concluiu ou concluirá o Ensino Médio), será desconsiderada do estudo por conter mais de 30% dos valores ausentes.

Tabela 1. Porcentagem de Dados Ausentes por Colunas do Dataset
Fonte: Resultados originais da pesquisa

## Tipos de Variáveis:

Um passo muito importante da etapa de tratamento é entender quais são os tipos das variáveis do conjunto de dados, separando e analisando-as individualmente, quais são quantitativas e quais são qualitativas.

Tabela 2. Variáveis do Dataset e seus tipos
Fonte: Resultados originais da pesquisa

As próximas etapas de tratamento foram separadas por tipo das variáveis:

## Quantitativas

### Tratamento de Outliers

Os outliers são os dados que estão muito distantes da maioria dos dados analisados, uma forma de visualizar os outliers seria pela representação do Gráfico de Box-plot.
No gráfico de Box-Plot, pode-se ter informações importantes sobre o comportamento dos dados, tanto a mediana e os quartis, quando analisar os limites superiores e inferiores, identificando os outliers como valores fora desses limites


Figura 2. Representação do Gráfico de Box-Plot
Fonte: ICMC JÚNIOR (2021)

Abaixo um exemplo de uma das Colunas com Box-Plot gerado, onde analisa-se a posição da mediana por volta de 19, primeiro e terceiro quartil muito próximos da mediana, limite superior em torno de 30 e limite inferior 5, pela imagem tem-se muitos outliers, dados fora do limite superior.


Figura 3. Representação Box-Plot da Coluna Idade
Fonte: Resultados originais da pesquisa

É recomendado retirar os outliers do conjunto de dados para futura inserção no modelo, no caso deste estudo, após retirada dos outliers sobraram aproximadamente 200 dados no dataset, impossibilitando a continuação do estudo, então foi decidido manter os outliers para análise com essa quantidade grande de dados fora dos limites.

### Distribuição dos Dados:

Importante entender como os dados estão se comportando, nesse passo foram usados cálculos estatísticos para entender a distribuição dos dados.
Percebe-se no conjunto de dados uma quantidade grande de valores na média, ainda assim existe uma quantidade de dados dispersos que pelo que foi analisado anteriormente são os valores chamados de outliers, fora do intervalo de 3 desvios padrões da média. A maioria dos gráficos ficaram bem próximos de uma simetria com uma cauda alongada nas duas pontas, tendendo a se aproximar de uma curva normal, o único diferente desse padrão é o Gráfico da Idade e Quantidade Pessoas na Residência que é assimétrico com a cauda alongada à direita.
Na Figura 4, tem-se Coluna Idade com Coeficiente de Variação de 32.76%, Assimetria de 2.24 e Curtose de 5.63, indicando uma assimétrica positiva e curva com distribuição alongada

Figura 4. Distribuição da Coluna Idade
Fonte: Resultados originais da pesquisa

Na Figura 5, tem-se Coluna Nota Ciências da Natureza com Coeficiente de Variação de 13.72%, Assimetria de 0.42 e Curtose de 0.91, indicando uma simetria e curva com distribuição normal.

Figura 5. Distribuição da Coluna Nota Ciências da Natureza
Fonte: Resultados originais da pesquisa

Na Figura 6, tem-se Coluna Nota Ciências Humanas com Coeficiente de Variação de 14.31%, Assimetria de -0.56 e Curtose de 3.51, indicando uma simetria e curva com distribuição achatada.

Figura 6. Distribuição da Coluna Nota Ciências Humanas
Fonte: Resultados originais da pesquisa

Na Figura 7, tem-se Coluna Nota Linguagem e Comunicação com Coeficiente de Variação de 10.67%, Assimetria de -0.91 e Curtose de 4.51, indicando uma simetria  e curva com distribuição achatada.

Figura 7. Distribuição da Coluna Nota Linguagem e Comunicação
Fonte: Resultados originais da pesquisa

Na Figura 8, tem-se Coluna Nota Matemática com Coeficiente de Variação de 18.25%, Assimetria de 0.97 e Curtose de 1.05, indicando uma simetria  e curva com distribuição alongada.

Figura 8. Distribuição da Coluna Nota Matemática
Fonte: Resultados originais da pesquisa

Na Figura 9, tem-se Coluna Nota Redação com Coeficiente de Variação de 28.50% , Assimetria de -0.78 e Curtose de 2.75, indicando uma simetria  e curva com distribuição alongada.

Figura 9. Distribuição da Coluna Nota Redação
Fonte: Resultados originais da pesquisa

Na Figura 10, tem-se Coluna Quantidade Pessoas na Residência com Coeficiente de Variação de 38.66% , Assimetria de 1.21 e Curtose de 5.53, indicando uma assimetria positiva e curva com distribuição alongada.

Figura 10. Distribuição da Coluna Quantidade Pessoas na Residência
Fonte: Resultados originais da pesquisa

### Correlação

Para as variáveis quantitativas analisa-se a relação entre as variáveis (correlação) por meio da covariância e coeficiente de correlação de Pearson.
Na diagonal principal temos a correlação entre as mesmas variáveis, no caso uma correlação positiva perfeita.
Levando em consideração um valor de correlação alta em torno de 0.85, observa-se que no conjunto das variáveis no gráfico abaixo nenhum par de variáveis apresenta correlação igual ou maior ao valor apresentado, sendo assim não será descartada nenhuma variável por conta de correlação, gerando a posteriori problemas como a multicolinearidade.

Figura 11. Correlação Variáveis Quantitativas
Fonte: Resultados originais da pesquisa

## Qualitativas

### Correlação

A análise de correlação para variáveis qualitativas foi realizada através da estatística do qui-quadrado, por termos qualitativas nominais e ordinais.
Levando em consideração um valor de correlação alta em torno de 0.85, mesmo usado nas variáveis quantitativas, observa-se que no conjunto das variáveis no gráfico abaixo a variável NU_ANO apresenta correlação positiva perfeita com todas as outras variáveis (e é uma variável com valor único), então ela será retirada do conjunto de dados para não gerar a posteriori problemas como a multicolinearidade.


Figura 12. Correlação Variáveis Qualitativas
Fonte: Resultados originais da pesquisa

### Dummy

Alguns modelos tem como pré-requisito todas as variáveis estarem na forma numérica, no caso das variáveis qualitativas será necessário transformá-las em dados do tipo binário, no caso 0 ou 1 (sim/presença ou não/ausência), evitando assim a chamada Ponderação Arbitrária onde são atribuídos números que indicam quantidade ou dão peso a uma categoria.
No exemplo abaixo, a coluna TP_COR_RACA, possui 6 categorias, e no processo de transformação em variáveis binárias, foram adicionadas 5 colunas ao dataset (n - 1 dummies), onde n é a quantidade de categorias da variável, em cada coluna é verificada a existência ou não daquela variável para cada observação do dataset. Retirar uma das colunas ajuda a não ter colunas desnecessárias que poderão causar multicolinearidade, sendo possível a validação que, se uma observação estiver com todas as colunas 0 a coluna não adicionada seria o valor 1.



Figura 13. Processo de Transformação das Variáveis Qualitativas em Dummies
Fonte: Resultados originais da pesquisa

## Variável Dependente

Com base nos dados do Enem, foi adicionada três colunas, uma chamada NU_NOTA_MEDIA, calculada a partir das Notas: NU_NOTA_CN, NU_NOTA_CH, NU_NOTA_LC, NU_NOTA_MT, sem adicionar pesos específicos as notas, e sem a nota da redação (posteriormente adicionar validação se nota de redação não está zerada, e validar peso no resultado final do estudante).
Levando em consideração dados de notas de corte, foram adicionadas as colunas APPROVED_MED e APPROVED_ADM, que levam em consideração se a partir de uma nota de corte: 769 e 560 respectivamente, o estudante é aprovado ou não em Medicina ou em Administração.
Assim foi finalizado o processo de Tratamento dos Dados.

## Modelo

Algumas análises para a escolha do Modelo dentro dos GLM (Modelos Lineares Generalizados):
Considerando a variável Dependente APPROVED_ADM que é uma variável qualitativa, escolhe-se o Modelo Logístico (classificação), dentro dos modelos logísticos existe o multinomial e o binário, sendo escolhido o último por conta da variável se apresentar de maneira binária.
Obtendo-se o seguinte Modelo:
Modelo de Regressão Logística Binária com Distribuição de Bernoulli
Foi utilizada a biblioteca do SKLEARN LogisticRegression(), com os dados separados em y = Variável Dependente (variável APPROVED_ADM)  e X = Variáveis Independentes (todas menos a Dependente e a APPROVED_MED - que não foi utilizada nesse primeiro momento).
Dessa variáveis X e y, são separados os Dados de Treino e Teste, X_treino, X_teste, y_treino, y_teste, onde 30% dos dados foram separados para teste e 70% para treino.
O modelo é treinado (fit), geram-se as análises, a primeira será a Matriz de Confusão e depois a Curva ROC, as duas serão demonstradas prevendo com os mesmos dados de treino e também com os dados de teste.

### Matriz de Confusão	
	
A imagem a seguir serve para entender como funciona a matriz de confusão, que tem os Valores Reais (Verdadeiros) e os Valores Previstos, contabilizando o que o modelo acertou e errou, tanto em Ausência ou Presença de um Evento definido.


Figura 14. Explicação Matriz de Confusão
Fonte: BIOINFO UFPR (2021)

### Dados de Treino

Para os dados de Treino, a matriz de confusão gerou os seguintes resultados: 5721 de Verdadeiro Negativo (VN), 212 Falso Negativo (FN), 673 de Verdadeiro Positivo (VP) e 394 Falso Positivo (FP).
	Com os valores da Matriz de Confusão, podemos calcular índices importantes:
 	Acurácia, que mostra o quão Exato é o modelo: 
(VP+VN) / n = (673 + 5721) / 7000 = 0,9134
Poderia dizer que esse modelo com 91% de acurácia é bom (mas precisa ter outros modelos para comparação), mas a acurácia pode levar a conclusões errôneas sobre o modelo, se levada em consideração como medida de desempenho única.
 	Recall ou Sensibilidade, taxa de acerto de Evento, maior percentual, minimiza os falsos negativos:
VP / (VP+FP) = 673 / ( 673 + 394 ) = 0,6307
	Especificidade, taxa de acerto de Não Evento:
VN / (FN+VN) = 5721 / ( 212 + 5721 ) = 0,9643

Figura 15. Matriz de Confusão com Dados de Treino
Fonte: Resultados originais da pesquisa

	Com a Especificidade e a Sensibilidade obtém-se a Curva ROC (Receiver Operating Characteristic)
Considerando uma área abaixo da curva igual a 1, na análise da Curva ROC quanto mais próximo de 1 a área, melhor o modelo. O modelo com dados de treino tem uma área de 0.91.


Figura 16. Curva ROC com Dados de Treino
Fonte: Resultados originais da pesquisa

### Dados de Teste

Para os dados de Teste, a matriz de confusão gerou os seguintes resultados: 2432 de Verdadeiro Negativo (VN), 102 Falso Negativo (FN), 306 de Verdadeiro Positivo (VP) e 160 Falso Positivo (FP).
	Com os valores da Matriz de Confusão, podemos calcular índices importantes:
 	Acurácia, que mostra o quão Exato é o modelo: 
(VP+VN) / n = ( 306 + 2432 ) / 3000 = 0,9127
 	Recall ou Sensibilidade, taxa de acerto de Evento, maior percentual, minimiza os falsos negativos:
VP / (VP+FP) = 306 / ( 306 +  160 ) = 0,6567
	Especificidade, taxa de acerto de Não Evento:
VN / (FN+VN) = 2432 / ( 306 + 2432 ) = 0,8882


Figura 2. Matriz de Confusão com Dados de Teste
Fonte: Resultados originais da pesquisa

		Com a Especificidade e a Sensibilidade obtém-se a Curva ROC (Receiver Operating Characteristic)
Considerando uma área abaixo da curva igual a 1, na análise da Curva ROC quanto mais próximo de 1 a área, melhor o modelo. O modelo com dados de teste tem uma área de 0.93.

Figura 17. Curva ROC com Dados de Teste
Fonte: Resultados originais da pesquisa


### Previsão

* Analise 1 - Qual a porcentagem de chance de um Estudante do sexo Masculino, Branco, Solteiro, morador do Estado de São Paulo, com 18 anos, notas em torno de 700, 3 pessoas morando na casa e uma renda maior que R$ 19.000,00 passar no ENEM?
De acordo com o modelo gerado: Ele teria 80.61% de probabilidade de passar no ENEM.
* Analise 2 - E um homem negro nas mesmas condições anteriores?
De acordo com o modelo gerado: Ele teria 79.0% de probabilidade de passar no ENEM.
Com essas duas análises a Raça não tem tanto impacto na porcentagem de chance de passar no ENEM.
Porém, dá para levar em consideração que o resto das variáveis são iguais?

* Análise Racial

Com a Tabela 3 consegue-se ver que para os estudantes das Raças Preta (2) e Parda (3) as médias das notas são menores em comparação com estudantes da Raça Branca (1).

Tabela 3. Médias de Notas Agrupadas por Raça
Fonte: Resultados originais da pesquisa

Na Figura 18 foram agrupadas as Faixas de Renda das Famílias em relação às Raças e tem-se uma quantidade muito maior concentrada nas Faixas de Renda mais baixas da soma das Raças Preta e Parda em comparação com as outras.
E nas maiores faixas quase nenhuma representação.
É nítido no gráfico que na Faixa A predomina a Raça Parda, assim como na B, C e D.
A partir da Faixa E começa a inverter e a Raça Branca começa a dominar, não na mesma proporção, mas isso pode fazer a média de renda da Raça Branca ser maior que a Parda, que está concentrada nas faixas mais baixas.


Figura 18. Gráfico de Barras da Faixa de Renda Agrupada por Raça
Fonte: Resultados originais da pesquisa

Levando em consideração essa análise, será realizada nova previsão com base nesses dados analisados.

### Nova Previsão

* Análise 1 - Considerada para as Raças Pretas e Pardas: NU_NOTA_CN: 467,  NU_NOTA_CH: 498,  NU_NOTA_LC: 513,  NU_NOTA_MT: 503,  NU_NOTA_REDACAO 563, Média: 496 com Renda B
De acordo com o modelo gerado: Ele teria 16.98% de probabilidade de passar no ENEM.
* Análise 2 -  Considerado para a Raça Branca: NU_NOTA_CN: 492,  NU_NOTA_CH: 527,  NU_NOTA_LC: 538,  NU_NOTA_MT: 543,  NU_NOTA_REDACAO 605, Média: 525 com Renda G
De acordo com o modelo gerado: Ele teria 31.0% de probabilidade de passar no ENEM.
Percebe-se que nenhum dos casos tem grandes chances de passar no Enem por conta das notas, porém percebemos a diferença de valores em relação a raça.
Como pode aumentar essa porcentagem. A posteriori será realizada a experimentação de resultados baseado no Sistema de Cotas.
