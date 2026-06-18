import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # encodings principais:  utf-8, iso-8859-1, latin1, cp1252
    # https://docs.python.org/3/library/codecs.html#standard-encodings
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por munic
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()

    # ordenar por ordem decrescente
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)

    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# obter informações sobre padrão de roubo_veiculo
try:
    print('\nObtendo informações sobre padrão de roubo de veículos...')

    # array é uma estrutura de dados que armazena uma coleção de dados
    # e computacionalmente é mais eficiente para calcular estatísticas
    # Faz parte da biblioteca numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # mediana de roubo_veiculo
    # divide a distribuição em duas partes iguais (50% dos dados abaixo e 50% acima)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # distânicia
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)

    # Medidas de tendência central
    # Se a média for muito diferente da mediana, distribuição é assimétrica. Não tende a haver um padrão
    # Se a distância for menor que 10%, distribuição tende a ser simétrica. Tende a haver um padrão.
    # Se a distância for entre 10% a 25% a distribuição tende a uma assimetria moderada. Valores extremos podem estar influenciando na média. 
    # Se a distância for maior que 25%, distribuição tende a ser assimétrica. Valores extremos podem estar influenciando na média. 
    # A distribuição não tende a um padrão.
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia}')


    # Quartis
    # Método padrão é o weibull 
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull') # Q1 é 25% 
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull') # Q2 é 50% (mediana)
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull') # Q3 é 75%


    # MENORES ROUBOS
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo abaixo q1
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # MAIORES ROUBOS
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo acima q3
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicípios com qtdes menores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

    print('\nMunicípios com qtdes maiores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))


    # ------------------------ II - PARTE EXEMPLO 02  ------------------------
    # Medidas de dispersão
    # Amplitude total: Maior valor - menor valor
    # Quanto mais próximo de zero, maior a homogeneidade dos dados
    # Se for igual a zero, todos os valores são iguais.  
    # Quanto mais próximo do máximo, maior a dispersão dos dados ou heterogeneidade
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)


    # IQR (Intervalo interquartil)
    # é a amplitude do intervalo dos 50% dos dados centrais
    # Calcula-se: q3 - q1
    # Ela ignora os valores extremos. Max e min estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # quanto mais próximo do q3, mais heterogêneo são os dados
    iqr = q3 - q1

    # limite superior
    # vai identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior
    # vai identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)


    # medidas de posição (ou de dispersão)
    print('\nMedidas de posição: ')
    print(30*'-')
    print('Mínimo: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Máximo: ', maximo)
    

    # --------------------------------- ACHANDO OS OUTLIERS -------------------------------------
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo abaixo q1
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo acima q3
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nMunicípios com outliers inferiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))


    print('\nMunicípios com outliers superiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()


# visualizar os dados
try:
    print('Visualizando os dados...')

    plt.figure(figsize=(18, 10))
    plt.suptitle('Análise de Roubo de Veículos no RJ', fontsize=16)


    # ===================================================
    # POSIÇÃO 1 - 10 MAIORES VALORES
    # ===================================================
    plt.subplot(2, 2, 1)

    df_roubo_veiculo_maiores = (
        df_roubo_veiculo_maiores
        # .sort_values(by='roubo_veiculo', ascending=False)
        .head(10)
        .sort_values(by='roubo_veiculo', ascending=True)
    )

    plt.bar(
        # .str.slice(0, 10) No máximo, 10 caracteres
        df_roubo_veiculo_maiores['munic'].str.slice(0, 10), 
        df_roubo_veiculo_maiores['roubo_veiculo'])


    # COLOCAR OS RÓTULOS (GRÁF. COLUNAS)
    deslocamento = max(df_roubo_veiculo_maiores['roubo_veiculo']) * 0.01

    for i, valor in enumerate(df_roubo_veiculo_maiores['roubo_veiculo']):
        plt.text(
            i,  # posição x
            valor + deslocamento,  # posição y
            f'{valor:,}',
            ha='center',
        )

    plt.title('Top 10 - Municípios com maiores roubos')
    plt.xticks(rotation=45, ha='right')

    # ===================================================
    # POSIÇÃO 2 - 10 MENORES VALORES
    # ===================================================
    plt.subplot(2, 2, 2)

    # Se existirem outliers inferiores, exibe eles
    if len(df_roubo_veiculo_outliers_inferiores) > 0:

        df_roubo_veiculo_outliers_inferiores = (
            df_roubo_veiculo_outliers_inferiores
            .sort_values(by='roubo_veiculo', ascending=True)
        )

        plt.barh(
            df_roubo_veiculo_outliers_inferiores['munic'], 
            df_roubo_veiculo_outliers_inferiores['roubo_veiculo']
        )
        plt.title('Municípios com Outliers Inferiores')


    # Caso não existam, exibe os 10 menores valores
    else:
        df_roubo_veiculo_menores = (
            df_roubo_veiculo_menores
            .sort_values(by='roubo_veiculo', ascending=True)
            .head(10)
            .sort_values(by='roubo_veiculo', ascending=False)
        )

        plt.barh(
            df_roubo_veiculo_menores['munic'], 
            df_roubo_veiculo_menores['roubo_veiculo']
        )
        plt.title('Bottom 10 - Municípios com menores roubos')


    # ===================================================
    # POSIÇÃO 3 - BOXPLOT COM OUTLIERS E MÉDIA
    # ===================================================
    plt.subplot(2, 2, 3)

    # showfliers=False - remove os outliers
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)

    plt.title('Boxplot dos Roubos de Veículos')


    # ===================================================
    # POSIÇÃO 4 - MEDIDAS ESTATÍSTICAS
    # ===================================================
    plt.subplot(2, 2, 4)

    plt.text(0.1, 0.9, f'Média: {media_roubo_veiculo}', fontsize=10)
    plt.text(0.1, 0.8, f'Mediana: {mediana_roubo_veiculo}', fontsize=10)
    plt.text(0.1, 0.7, f'Distância: {distancia}', fontsize=10)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=10)
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=10)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=10)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=10)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=10)

    plt.axis('off')
    plt.title('Resumo Estatístico')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()