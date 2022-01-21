import mysql.connector as mysql
from config import config
import pandas as pd

conn = mysql.connect(**config)

mycursor = conn.cursor()

mycursor.execute("SELECT NU_INSCRICAO, NU_ANO,NU_IDADE, TP_COR_RACA, TP_ESTADO_CIVIL, TP_NACIONALIDADE, TP_SEXO, NO_MUNICIPIO_RESIDENCIA, SG_UF_RESIDENCIA, TP_ST_CONCLUSAO, TP_ENSINO,NU_NOTA_CN, NU_NOTA_CH,NU_NOTA_LC, NU_NOTA_MT, NU_NOTA_COMP1, NU_NOTA_COMP2, NU_NOTA_COMP3, NU_NOTA_COMP4, NU_NOTA_COMP5, NU_NOTA_REDACAO, IN_BRAILLE, IN_AMPLIADA_18, IN_AMPLIADA_24, IN_LEDOR, IN_ACESSO, IN_TRANSCRICAO, IN_LIBRAS, Q001, Q002, Q003, Q004, Q005, Q006 FROM enem_tcc LIMIT 2000")

myresult = mycursor.fetchall()

# 31 vars
dataframe = pd.DataFrame(columns=['NU_INSCRICAO', 'NU_ANO', 'NU_IDADE', 'TP_COR_RACA', 'TP_ESTADO_CIVIL', 'TP_NACIONALIDADE','TP_SEXO', 'NO_MUNICIPIO_RESIDENCIA', 'SG_UF_RESIDENCIA', 'TP_ST_CONCLUSAO', 'TP_ENSINO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'IN_BRAILLE', 'IN_AMPLIADA_18', 'IN_AMPLIADA_24', 'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS', 'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006'])

#dataframe = pd.DataFrame()
for row in myresult:
  dados_linha = '["%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"]' %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]), str(row[20]), str(row[21]), str(row[22]), str(row[23]), str(row[24]), str(row[25]), str(row[26]), str(row[27]), str(row[28]), str(row[29]), str(row[30]), str(row[31]), str(row[32]), str(row[33]))
  dados_linha_lista = eval(dados_linha)

  dados_lista = []

  for x in dados_linha_lista:
    string = x.replace("'","")
    dados_lista.append(string)

  a_series = pd.Series(dados_lista, index = dataframe.columns)
  dataframe = dataframe.append(a_series, ignore_index=True)


dataframe.to_csv("src/enem_2019.csv")
