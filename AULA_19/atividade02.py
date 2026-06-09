import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando somente as variáveis necessárias
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    # Totalizar estelionato por mês/ano
    df_estelionato = df_estelionato.groupby('mes_ano', as_index=False)['estelionato'].sum()

    print(df_estelionato.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# obter informações sobre padrão de estelionato
try:
    print('Obtendo informações sobre padrão de estelionato...')

    # Converter para array numpy
    array_estelionato = np.array(df_estelionato['estelionato'])

    # Média e mediana
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)

    # Distância relativa entre média e mediana
    distancia = abs((media - mediana) / mediana)

    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de estelionatos: {media}')
    print(f'Mediana de estelionatos: {mediana}')
    print(f'Distância entre média e mediana: {distancia}')


    # Quartis (Weibull)
    q1 = np.quantile(array_estelionato, 0.25, method='weibull')
    q2 = np.quantile(array_estelionato, 0.50, method='weibull')
    q3 = np.quantile(array_estelionato, 0.75, method='weibull')

   
    # Mairores e menores estelionatos
    print('\nMeses/Ano com menores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]
    print(df_estelionato_menores.sort_values(by='estelionato'))

    print('\nMeses/Ano com maiores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]
    print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False))


    # ------------------------ II - PARTE EXEMPLO 02 ------------------------
    # IQR
    iqr = q3 - q1


    # Cálculo dos limites para outliers
    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)


    # ----------------------------------------------
    # Medidas de dispersão
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)
    # -----------------------------------------------

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


    # ---------------------------- ACHANDO OS OUTLIERS -------------------------
    df_outliers_inferiores = df_estelionato[df_estelionato['estelionato'] < limite_inferior]
    df_outliers_superiores = df_estelionato[df_estelionato['estelionato'] > limite_superior]

    print('\nMeses/Ano com outliers inferiores: ')
    print(30*'-')
    if len(df_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_outliers_inferiores.sort_values(by='estelionato'))

    print('\nMeses/Ano com outliers superiores: ')
    print(30*'-')
    if len(df_outliers_superiores) == 0:
        print('Não existem outliers superiores!')
    else:
        print(df_outliers_superiores.sort_values(by='estelionato', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()



# plotar gráfico dos maiores
try:
    # 10 maiores estelionatos ordenados
    df_estelionato_maiores = (
        df_estelionato_maiores
        .sort_values(by='estelionato', ascending=False)
        .head(30)
    )

    plt.barh(
        df_estelionato_maiores['mes_ano'],
        df_estelionato_maiores['estelionato'],
        color='blue'
    )

    # Mostrar os valores ao final das barras
    for i, valor in enumerate(df_estelionato_maiores['estelionato']):
        plt.text(
            valor,      # posição x
            i,          # posição y
            f' {valor:,}',
            va='center'
        )

    plt.title('10 maiores quantidades de estelionato')
    plt.show()

except Exception as e:
    print(f'Erro ao plotar gráfico: {e}')
    exit()



# Plotagem gráfica dos menores
try:
    # ordenando em decrescente e filtrando
    df_estelionato_menores = (
        df_estelionato_menores
        .sort_values(by='estelionato', ascending=True)
        .head(20)
        .sort_values(by='estelionato', ascending=False)
    )

    plt.barh(
        df_estelionato_menores['mes_ano'],
        df_estelionato_menores['estelionato']
    )

    # Mostrar os valores ao final das barras
    for i, valor in enumerate(df_estelionato_menores['estelionato']):
        plt.text(
            valor,
            i,
            f' {valor:,}',
            va='center'
        )

    plt.title('10 menores quantidades de estelionato')
    plt.show()

except Exception as e:
    print(f'Erro ao plotar gráfico: {e}')
    exit()




# visualizar os dados
try:
    print('Visualizando os dados...')

    # criar painel com 2 gráficos
    plt.subplots(2, 1, figsize=(16, 7))
    plt.suptitle('Análise de estelionatos no RJ')


    # ---------------------------------------------------
    # POSIÇÃO 1: Menores quantidades de estelionato
    # ---------------------------------------------------
    plt.subplot(2, 1, 1)

    df_menores_grafico = (
        df_estelionato_menores
        .sort_values(by='estelionato', ascending=True)
        .head(10)
        .sort_values(by='estelionato', ascending=False)
    )

    plt.barh(
        df_menores_grafico['mes_ano'],
        df_menores_grafico['estelionato']
    )

    plt.title('Ranking dos meses com menores quantidades de estelionato')


    # ---------------------------------------------------
    # POSIÇÃO 2: Maiores quantidades de estelionato
    # ---------------------------------------------------
    plt.subplot(2, 1, 2)

    df_maiores_grafico = (
        df_estelionato_maiores
        .sort_values(by='estelionato', ascending=True)
        .head(10)
    )

    plt.barh(
        df_maiores_grafico['mes_ano'],
        df_maiores_grafico['estelionato']
    )

    plt.title('Ranking dos meses com maiores quantidades de estelionato')

    # ajustar layout
    plt.tight_layout()

    # exibir painel
    plt.show()

except Exception as e:
    print(f'Erro ao visualizar os dados: {e}')
    exit()

    