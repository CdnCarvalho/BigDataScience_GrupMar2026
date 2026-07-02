import polars as pl
import numpy as np
import matplotlib.pyplot as plt


# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # leitura com polars
    df_ocorrencias = pl.read_csv(ENDERECO_DADOS, separator=';', encoding='iso-8859-1')

    # delimitando somente as variáveis
    df_lesoes = df_ocorrencias.select(['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte'])

    # Totalizar
    df_total_lesoes = (
        df_lesoes.group_by('cisp')
        .agg([
            pl.col('lesao_corp_dolosa').sum(),
            pl.col('lesao_corp_morte').sum()
        ])
    )

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