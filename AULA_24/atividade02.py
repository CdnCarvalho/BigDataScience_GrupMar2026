import pandas as pd
import polars as pl
from datetime import datetime
import gc  #  Garbage Collector
# import os


ENDERECO_DADOS = r'../dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    lista_arquivos = ['202602_NovoBolsaFamilia.csv', '202603_NovoBolsaFamilia.csv']

    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        # PANDAS
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')
        
        # POLARS
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        # Concatenação de dataframes
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        # Prints
        print(df.head())
        # print(df.shape)  # Total de Colunas e Linhas
        # print(df.columns)  # Nomes das Colunas | Pandas .columns.tolist()
        # print(df.dtypes)  # Tipos das Colunas

        # limpar df da memória
        del df        
        
        # Coletar resíduos da memória, após variável deixar de existir na memória
        gc.collect()

    fim = datetime.now()

    print('\nBolsa Família Concatenado')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)

    print(f'Tempo de execução: {fim - inicio}')

except Exception as e:
    print(f'Erro ao importar os arquivos: {e}')