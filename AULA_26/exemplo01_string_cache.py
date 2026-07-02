import polars as pl
import numpy as np
from datetime import datetime 
# from scipy.stats import kurtosis, skew
import matplotlib.pyplot as plt


# Não mostrar números científicos
pl.Config.set_fmt_float("full")


# ENDERECO_DADOS = r'./AULA-13/PARQUET/'
ENDERECO_DADOS = r'C:/dados/novo_bolsa_familia/'
# ENDERECO_DADOS = r'C:/dados/auxilio_brasil/'

try:
    print('\nIniciando processamento com plano Lazy...')
    inicio = datetime.now()

    # O "with pl.StringCache():" foi removido. 
    # O Polars gerencia o .cast(pl.Categorical) abaixo automaticamente de forma otimizada.
    plano_execucao_lazy = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        # pl.scan_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        .with_columns([            
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)  ## Converte município para Categorical - economia de RAM           
            # pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
        ])
        # .filter(pl.col('VALOR PARCELA') > 2000)
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort('VALOR PARCELA', descending=True)
    )

    # Executamos o plano p/ trazer os dados
    df_bolsa_familia = plano_execucao_lazy.collect()

    print(df_bolsa_familia.head(10))

    fim = datetime.now()
    print('Leitura do Parquet realizada com sucesso!')
    print(f'Tempo de execução: {fim - inicio}')

except Exception as e:
    print(f'Erro ao processar os dados: {e}')


# Impressão de números grandes com notação científica
    # e6: Casa dos Milhões (ex: 1e6 = 1.000.000)
    # e7: Dezena de Milhões (ex: 1e7 = 10.000.000)
    # e8: Centena de Milhões (ex: 1e8 = 100.000.000)
    # e9: Casa dos Bilhões (ex: 1e9 = 1.000.000.000)


