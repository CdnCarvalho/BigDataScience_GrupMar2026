# LENDO ARQUIVO PARQUET
import polars as pl
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# ENDERECO_DADOS = r'../bronze/'
ENDERECO_DADOS = r'./PARQUET/'

try:
    print('\nIniciando leitura do arquivo parquet...')
    inicio = datetime.now()  # Pega o tempo inicial

    # Gera o plano de execução para leitura do arquivo parquet
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  # Polars - leitura direta
    
    # Executa o plano de execução para obter o DataFrame
    df_bolsa_familia = df_plano_execucao.collect()

    print(df_bolsa_familia.head(10))
    print('\nArquivo parquet lido com sucesso!')

    fim = datetime.now()  # Pega o tempo final
    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
except Exception as e:
    print(f'Erro ao ler os dados do parquet: {e}')


# Processando as informações
try:
    hora_inicio = datetime.now()
    
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])  # criar um array com o valor da parcela
except Exception as e:
    print(f'Erro ao obter dados: {e}')


# Visualizar a distribuição - Boxplot
try:
    print('Visualizando a distribuição dos valores das parcelas em um boxplot...')

    # criar um boxplot
    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição dos valores das parcelas')

    # marcar a hora de término
    hora_fim = datetime.now()
    print(f'Tempo de execução: {hora_fim - hora_inicio}')

    plt.show()

except Exception as e:
    print(f'Erro ao visualizar dados: {e}')