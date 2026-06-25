# pip install polars
import pandas as pd
import polars as pl
from datetime import datetime

# Recomendo acessar o site oficial para instalação do polars. http://pola.rs
# É uma biblioteca de manipulação de dados em larga escala, muito mais rápida
# que o pandas. Foi desenvolvida em Rust.
# O processamento de dados é feito em paralelo, o que é muito mais eficiente 
# que o processamento sequencial do pandas.
# A polars tem um motor de execução Multithread, que permite a execução
# de operações em paralelo.

# pandas: Tempo de execução: 0:01:12.719990

try:
    # ENDERECO_DADOS = r'./dados/'
    ENDERECO_DADOS = r'../dados/'

    # Tempo de iníncial
    hora_import = datetime.now()

    print('Carregando...')

    # Pandas
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202602_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')

    # Polars
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202602_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head())


    # No Pandas
    # print('Nomes das colunas:', df_janeiro.columns.tolist())

    # No Polars - não precisa do .tolist()
    print('Nomes das colunas:', df_janeiro.columns)

    # Tempo final
    hora_impressao = datetime.now()

    print(f"Tempo de execução: {hora_impressao - hora_import}")

    # ((tempo_pandas - tempo_polars) / tempo_pandas) * 100  calculadora
    
except Exception as e:
    print("Erro ao obter dados: ", e)

