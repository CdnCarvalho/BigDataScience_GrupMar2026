# LENDO ARQUIVO PARQUET
import pandas as pd
from datetime import datetime
import polars as pl

# ENDERECO_DADOS = r'../bronze/'
ENDERECO_DADOS = r'./PARQUET/'

try:
    print('\nIniciando leitura do arquivo parquet...')
    inicio = datetime.now()  # Pega o tempo inicial

    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')    # Pandas
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  # Polars - leitura direta
    
    # imprimir em ordem decrescente
    print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(10))
    print('\nArquivo parquet lido com sucesso!')

    fim = datetime.now()  # Pega o tempo final
    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler os dados do parquet: {e}')



try:
    # Processar os dados do DataFrame
    print('\nIniciando processamento dos dados do DataFrame...')

    # Exemplo de processamento: Filtrar os registros onde o valor da parcela é maior que 100
    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA') > 2500)

    print(df_filtrado.shape)  # qtd linhas e colunas do df_filtrado

    print(f'\nNúmero de registros com valor da parcela maior que 2500: {df_filtrado.shape[0]}')
    print(df_filtrado.head())


except Exception as e:
    print(f'Erro ao processar os dados: {e}')