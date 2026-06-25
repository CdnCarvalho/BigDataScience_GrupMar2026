import pandas as pd
import polars as pl
from datetime import datetime
import gc  #  Garbage Collector
# import os

# Pandas Tempo de execução: 0:01:09.272633 - 0:03:40.311191
# Polars Tempo de execução: 0:00:35.855072 - 0:00:44.743114

ENDERECO_DADOS = r'../dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    lista_arquivos = ['202601_NovoBolsaFamilia.csv', '202602_NovoBolsaFamilia.csv']

    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        # PANDAS
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')
        
        # POLARS
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        print(df.head())

        # Concatenação de dataframes
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        # limpar df da memória
        del df        
        
        # Coletar resíduos da memória, após variável deixar de existir na memória
        gc.collect()

    fim = datetime.now()

    print('\nBolsa Família Concatenado')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)
    # print(df.columns)  # Nomes das Colunas | Pandas .columns.tolist()
    # print(df.dtypes)  # Tipos das Colunas

    print(f'Tempo de execução: {fim - inicio}')

except Exception as e:
    print(f'Erro ao importar os arquivos: {e}')