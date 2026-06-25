# import pandas as pd
from datetime import datetime
import polars as pl
import gc  # Garbage Collector
import os


ENDERECO_DADOS = r'../dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    df_bolsa_familia = None

    # Lista para receber CSVs, que serão processados
    lista_arquivos = []

    # Lista de todos os arquivos, que vieram do diretório
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    # Pegando os arquivos CSVs do diretório
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    print(lista_arquivos)

    # Leitura dos arquivos
    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}...')

        # Leitura de cada um dos dataframes
        df = pl.read_csv(
            ENDERECO_DADOS + arquivo, 
            separator=';', 
            encoding='iso-8859-1'
        )
        
        print(df.head())


        # Concatenação dos Dataframes
        # Verifica se o DataFrame df_bolsa_familia está vazio,
        # Se estiver vazio, "é que o Loop está na primeira execução", então
        # o df_dados é atribuído ao df_bolsa_familia.
        # Caso contrário, Se for diferente de None, acontece a concatenação,
        # pois neste caso, já teremos, pelo menos 1 dataframe no df_bolsa_familia atribuido.
        # Concatenação de dataframes
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        # Remover df_dados após o uso para liberar memória
        del df
        
        print(f'Arquivo {arquivo} processados com sucesso!')

        # Prints
        print(df_bolsa_familia.shape)

        print('\nDados dos DataFrames concatenados com sucesso!')

        # ######  Fim do laço For


    # Converte a coluna 'VALOR PARCELA' para o tipo float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )

    print('Incinando a gravação do arquivo Parquet...')

    # # Criar a pasta bronze se não existir
    # os.makedirs('../bronze', exist_ok=True)

    # Gravar o arquivo parquet
    df_bolsa_familia.write_parquet('../dados/bronze/bolsa_familia.parquet')
    # df_bolsa_familia.write_parquet('D:/bronze/bolsa_familia.parquet')
    
    print('\nBolsa Família Concatenado')
    print(df_bolsa_familia.shape)
    # print(df_bolsa_familia.head())

    # Deletar df_bolsa_familia da memória
    del df_bolsa_familia

    # Coletar resíduos da memória
    gc.collect()

    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')
    print('Gravação do arquivo Parquet realizada com sucesso!')

except ImportError as e:
    print(f'Erro ao processar os dataframes: {e}')