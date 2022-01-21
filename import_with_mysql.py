import mysql.connector as mysql
from mysql.connector import Error
from config import config
import csv

try:
    conn = mysql.connect(**config)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS enem_tcc;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE enem_tcc( NU_INSCRICAO VARCHAR(50), NU_ANO VARCHAR(50), NU_IDADE VARCHAR(50), TP_SEXO VARCHAR(50), TP_COR_RACA VARCHAR(50), TP_ESTADO_CIVIL VARCHAR(50), TP_NACIONALIDADE VARCHAR(50), CO_MUNICIPIO_RESIDENCIA VARCHAR(50), NO_MUNICIPIO_RESIDENCIA VARCHAR(50), CO_UF_RESIDENCIA VARCHAR(50), SG_UF_RESIDENCIA VARCHAR(50), TP_ST_CONCLUSAO VARCHAR(50), TP_ENSINO VARCHAR(50), CO_ESCOLA VARCHAR(50), CO_MUNICIPIO_ESC VARCHAR(50), NO_MUNICIPIO_ESC VARCHAR(50), CO_UF_ESC VARCHAR(50), SG_UF_ESC VARCHAR(50), TP_DEPENDENCIA_ADM_ESC VARCHAR(50), TP_LOCALIZACAO_ESC VARCHAR(50), TP_SIT_FUNC_ESC VARCHAR(50), CO_MUNICIPIO_PROVA VARCHAR(50), NO_MUNICIPIO_PROVA VARCHAR(50), CO_UF_PROVA VARCHAR(50),    SG_UF_PROVA VARCHAR(50), TP_PRESENCA_CN VARCHAR(50), TP_PRESENCA_CH VARCHAR(50), TP_PRESENCA_LC VARCHAR(50), TP_PRESENCA_MT VARCHAR(50), NU_NOTA_CN VARCHAR(50), NU_NOTA_CH VARCHAR(50), NU_NOTA_LC VARCHAR(50), NU_NOTA_MT VARCHAR(50), TX_RESPOSTAS_CN VARCHAR(50), TX_RESPOSTAS_CH VARCHAR(50), TX_RESPOSTAS_LC VARCHAR(255), TX_RESPOSTAS_MT VARCHAR(50), CO_PROVA_CN VARCHAR(50), CO_PROVA_CH VARCHAR(50), CO_PROVA_LC VARCHAR(50), CO_PROVA_MT VARCHAR(50), TX_GABARITO_CN VARCHAR(50), TX_GABARITO_CH VARCHAR(50), TX_GABARITO_LC VARCHAR(255), TX_GABARITO_MT VARCHAR(50), TP_STATUS_REDACAO VARCHAR(50), NU_NOTA_COMP1 VARCHAR(50), NU_NOTA_COMP2 VARCHAR(50), NU_NOTA_COMP3 VARCHAR(50), NU_NOTA_COMP4 VARCHAR(50), NU_NOTA_COMP5 VARCHAR(50), NU_NOTA_REDACAO VARCHAR(50), IN_BRAILLE VARCHAR(50), IN_AMPLIADA_18 VARCHAR(50), IN_AMPLIADA_24 VARCHAR(50), IN_LEDOR VARCHAR(50), IN_ACESSO VARCHAR(50), IN_TRANSCRICAO VARCHAR(50), IN_LIBRAS VARCHAR(50), Q001 VARCHAR(50), Q002 VARCHAR(50), Q003 VARCHAR(50), Q004 VARCHAR(50), Q005 VARCHAR(50), Q006 VARCHAR(50), Q007 VARCHAR(50), Q008 VARCHAR(50), Q009 VARCHAR(50), Q010 VARCHAR(50), Q011 VARCHAR(50), Q012 VARCHAR(50), Q013 VARCHAR(50), Q014 VARCHAR(50), Q015 VARCHAR(50), Q016 VARCHAR(50), Q017 VARCHAR(50), Q018 VARCHAR(50), Q019 VARCHAR(50), Q020 VARCHAR(50), Q021 VARCHAR(50), Q022 VARCHAR(50), Q023 VARCHAR(50), Q024 VARCHAR(50), Q025 VARCHAR(50))")
            
        print("Table is created....")

        input_file = csv.DictReader(open("base_dados/enem/microdados_enem2019/Dados/MICRODADOS_ENEM_2019.csv", newline=''), delimiter=';')

        for row in input_file:
            cursor.execute('INSERT INTO enem_tcc values ("%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s")',
            (row['NU_INSCRICAO'], 
            row['NU_ANO'], row['NU_IDADE'], row['TP_SEXO'], row['TP_COR_RACA'], row['TP_ESTADO_CIVIL'], row['TP_NACIONALIDADE'], row['CO_MUNICIPIO_RESIDENCIA'] , row['NO_MUNICIPIO_RESIDENCIA'] , row['CO_UF_RESIDENCIA'] , row['SG_UF_RESIDENCIA'] , 
            row['TP_ST_CONCLUSAO'] , row['TP_ENSINO'] , row['CO_ESCOLA'] , row['CO_MUNICIPIO_ESC'] , row['NO_MUNICIPIO_ESC'] , row['CO_UF_ESC'] , row['SG_UF_ESC'] , 
            row['TP_DEPENDENCIA_ADM_ESC'] , row['TP_LOCALIZACAO_ESC'] , row['TP_SIT_FUNC_ESC'] , row['CO_MUNICIPIO_PROVA'] , row['NO_MUNICIPIO_PROVA'] , row['CO_UF_PROVA'] , 
            row['SG_UF_PROVA'] , row['TP_PRESENCA_CN'] , row['TP_PRESENCA_CH'] , row['TP_PRESENCA_LC'] , row['TP_PRESENCA_MT'] , row['NU_NOTA_CN'] , row['NU_NOTA_CH'] , 
            row['NU_NOTA_LC'] , row['NU_NOTA_MT'] , row['TX_RESPOSTAS_CN'] , row['TX_RESPOSTAS_CH'] , row['TX_RESPOSTAS_LC'] , row['TX_RESPOSTAS_MT'] , row['CO_PROVA_CN'] , 
            row['CO_PROVA_CH'] , row['CO_PROVA_LC'] , row['CO_PROVA_MT'] , row['TX_GABARITO_CN'] , row['TX_GABARITO_CH'] , row['TX_GABARITO_LC'] , row['TX_GABARITO_MT'] , 
            row['TP_STATUS_REDACAO'] , row['NU_NOTA_COMP1'] , row['NU_NOTA_COMP2'] , row['NU_NOTA_COMP3'] , row['NU_NOTA_COMP4'] , row['NU_NOTA_COMP5'] , row['NU_NOTA_REDACAO'] , 
            row['IN_BRAILLE'] , row['IN_AMPLIADA_18'], row['IN_AMPLIADA_24'] , row['IN_LEDOR'] , row['IN_ACESSO'] , row['IN_TRANSCRICAO'] , row['IN_LIBRAS'] , 
            row['Q001'] , row['Q002'] , row['Q003'] , row['Q004'] , row['Q005'] , row['Q006'] , row['Q007'] , row['Q008'] , row['Q009'] , row['Q010'] , row['Q011'] , 
            row['Q012'] , row['Q013'] , row['Q014'] , row['Q015'] , row['Q016'] , row['Q017'] , row['Q018'] , row['Q019'] , row['Q020'] , row['Q021'] , row['Q022'] , 
            row['Q023'] , row['Q024'] , row['Q025']))
            
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
