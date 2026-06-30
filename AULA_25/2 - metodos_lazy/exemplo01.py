import polars as pl
# import numpy as np
from datetime import datetime
# import matplotlib.pyplot as plt

ENDERECO_DADOS = r'./AULA-13/PARQUET/'

try:
    print('\nIniciando processamento Lazy...')
    inicio = datetime.now()

    # DEFINIÇÃO DO PLANO (LAZY)
    # Aqui não lemos os dados ainda, apenas definimos o que queremos.
    lazy_plan = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        # Selecionamos apenas as colunas necessárias ANTES de qualquer coisa
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        # Se precisar tratar a coluna:
        # .with_columns(
        #     pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
        # )
        # Agrupamento e soma
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        # Ordenação
        .sort('VALOR PARCELA', descending=True)
    )

    # EXECUÇÃO (COLLECT)
    # O Polars vai ler o arquivo já filtrando as colunas e agregando. 
    # Isso economiza memória e tempo.
    df_bolsa_familia = lazy_plan.collect()

    print(df_bolsa_familia.head(10))

    fim = datetime.now()
    print(f'Tempo de execução: {fim - inicio}')
    print('Gravação do arquivo Parquet realizada com sucesso!')

except Exception as e:
    print(f'Erro ao processar os dados: {e}')