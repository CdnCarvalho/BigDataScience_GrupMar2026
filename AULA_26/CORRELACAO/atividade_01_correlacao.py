import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis
    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # Agrupando por CISP e totalizando as lesões
    df_total_lesoes = df_lesoes.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    print(df_total_lesoes.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# correlação
try:
    print('Calculando a correlação...')

    # correlação de pearson
    correlacao = np.corrcoef(df_total_lesoes['lesao_corp_dolosa'], df_total_lesoes['lesao_corp_morte'])[0,1]

    print(f'Correlação: {correlacao}')

    # plotar gráfico
    plt.scatter(df_total_lesoes['lesao_corp_dolosa'], df_total_lesoes['lesao_corp_morte'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Lesão corporal dolosa')
    plt.ylabel('Lesão corporal seguida de morte')

    plt.show()

except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()