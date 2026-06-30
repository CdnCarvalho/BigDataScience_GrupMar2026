import pandas as pd 
import polars as pl
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
# pip install scipy
from scipy.stats import kurtosis, skew 


# ENDERECO_DADOS = '202501_NovoBolsaFamilia.csv'
ENDERECO_DADOS = './../../Aula-12/POLARS/202501_NovoBolsaFamilia.csv'
ENDERECO_DADOS = r'./dados/202501_NovoBolsaFamilia.csv'

try:

    # Tempo de iníncial
    hora_import = datetime.now()
    print('Carregando...')

    # Polars
    df_bolsa_familia = pl.read_csv(ENDERECO_DADOS, separator=';', encoding='iso-8859-1')
    print(df_bolsa_familia.head())

    # Tempo final
    hora_impressao = datetime.now()
    print(f"Tempo de execução: {hora_impressao - hora_import}")
    
except Exception as e:
    print("Erro ao obter dados: ", e)


try:
    # PRÉPROCESSAMENTO - TRANSFORMAÇÃO
    # POLARS
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',','.').cast(pl.Float64)
    )

    # PRÉPROCESSAMENTO - TRANSFORMAÇÃO
    # delimitando as colunas para exibir: NOME MUNICÍPIO, VALOR PARCELA
    df_bolsa_familia = df_bolsa_familia[['NOME MUNICÍPIO', 'VALOR PARCELA']]

    # PROCESSAMENTO - TRANSFORMAÇÃO
    # POLARS
    df_bolsa_familia = (
        df_bolsa_familia.group_by('NOME MUNICÍPIO').agg(pl.col('VALOR PARCELA').sum())
        )

    # PROCESSAMENTO - TRANSFORMAÇÃO (Pensar no pré-processamento como o esforço necessário para deixar os dados "utilizáveis" e "limpos".)
    # POLARS 
    df_bolsa_familia = df_bolsa_familia.sort(by='VALOR PARCELA', descending=True)
    print(df_bolsa_familia.head(10))

except Exception as e:
    print("Erro ao Converter Valor da Parcela: ", e)


# TRANSFORMAÇÃO
# Calculando Medidas
try:
    array_valores = np.array(df_bolsa_familia['VALOR PARCELA'])
    
    # Média e Mediana
    media = np.mean(array_valores)
    mediana = np.median(array_valores)
    distancia_media_mediana = abs((media - mediana) / mediana)

    print('\nMedidas de Tendência Central')
    print(30*'-')
    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Distância média-mediana: {distancia_media_mediana}')


    # ---------------- QUARTIS ----------------
    q1 = np.quantile(array_valores, 0.25, method='weibull')
    q2 = np.quantile(array_valores, 0.50, method='weibull')
    q3 = np.quantile(array_valores, 0.75, method='weibull')

    print('\nMedidas de Posição')
    print(30*'-')
    print(f'Q1 (25%): {q1:,.2f}')
    print(f'Q2 - (50%): {q2:,.2f}')
    print(f'Q3 (75%): {q3:,.2f}')


    # ---------------- MÁX, MIN E AMPLITUDE ----------------
    maximo = np.max(array_valores)
    minimo = np.min(array_valores)
    amplitude_total = maximo - minimo

    print('\nExtremos e Amplitude')
    print(30*'-')
    print(f'Mínimo: {minimo:,.2f}')
    print(f'Máximo: {maximo:,.2f}')
    print(f'Amplitude Total: {amplitude_total:,.2f}')


    # ---------------- IQR E LIMITES ----------------
    iqr = q3 - q1
    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    print('\nIntervalo Interquartil (IQR)')
    print(30*'-')
    print(f'IQR (Q3 - Q1): {iqr:,.2f}')
    print(f'Limite Inferior: {limite_inferior:,.2f}')
    print(f'Limite Superior: {limite_superior:,.2f}')



    # POLARS
    # ---------------- MAIORES (acima de Q3) ----------------
    df_maiores = (df_bolsa_familia
        .filter(pl.col('VALOR PARCELA') > q3)
        .sort('VALOR PARCELA', descending=True)
    )

    print('\nMunicípios acima de Q3 (25% superiores)')
    print(30*'-')
    print(df_maiores)


    # POLARS
    # ---------------- MENORES (abaixo de Q1) ----------------
    df_menores = (df_bolsa_familia
        .filter(pl.col('VALOR PARCELA') < q1)
        .sort('VALOR PARCELA', descending=False)
    )

    print('\nMunicípios abaixo de Q1 (25% inferiores)')
    print(30*'-')
    print(df_menores)


    # POLARS
    df_outliers_superiores = (df_bolsa_familia
        .filter(pl.col('VALOR PARCELA') > limite_superior)
    )

    df_outliers_inferiores = (df_bolsa_familia
        .filter(pl.col('VALOR PARCELA') < limite_inferior)
    )

    print('\nOutliers Superiores:')
    print(30*'-')
    print(df_outliers_superiores)

    print('\nOutliers Inferiores:')
    print(30*'-')
    print(df_outliers_inferiores)


    # ---------------- MEDIDAS DE VARIAÇÃO ----------------
    variancia = np.var(array_valores)
    desvio_padrao = np.std(array_valores)
    coef_variacao = desvio_padrao / media
    distancia_variancia_media = variancia / media


    # ---------------- ASSIMETIA E CURTOSE -----------------
    # ASSIMETRIA
    # Assimetria mede para que lado a cauda é mais longa e mais pesada
    # Concentração muito grande de municípios com valores relativamente menores
    # Pouquíssimos municípios com valores extremamente altos
    # A média está sendo fortemente puxada para cima
    # Presença de valores extremos muito grandes
    #   --- A cauda está à direita Existem valores muito altos
    #   --- Poucos municípios puxam a média para cima
    #   --- A média é maior que a mediana

    # PANDAS
    # assimetria = df_bolsa_familia['VALOR PARCELA'].skew()

    # POLARS
    # assimetria = df_bolsa_familia.select(
    #     pl.col('VALOR PARCELA').skew()
    # ).item()

    # COM SCIPY
    assimetria = skew(array_valores) 


    # CURTOSE
    # A curtose mede o peso das caudas, OU SEJA,
    # ----- Quão extremos são os valores que estão longe do centro.
    # Muitos municípios com valores relativamente próximos
    # Pouquíssimos municípios com valores absurdamente maiores
    # Presença de outliers extremamente distantes
    # Distribuição com pico muito acentuado
    # ""    A curtose extremamente elevada indica forte concentração dos dados 
    #       em torno de valores menores, combinada com a presença de poucos 
    #       municípios com valores excepcionalmente altos.  ""
    #   --- A cauda direita não é apenas longa. Ela é muito pesada 
    #   --- Existem valores absurdamente distantes do restante
    
    # PANDAS
    # curtose_valor = df_bolsa_familia['VALOR PARCELA'].kurt()

    # POLARS
    # curtose_valor = df_bolsa_familia.select(
    #     pl.col('VALOR PARCELA').kurtosis()
    # ).item()

    # COM SCIPY
    curtose_valor = kurtosis(array_valores)  

    # Outra opção para curtose é usar a função do scipy.stats
    # pip install scipy
    # from scipy.stats import kurtosis
    # assimetria = skew(array_valores)
    # curtose_valor = kurtosis(array_valores)


    print('\nMedidas de Variação')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Desvio Padrão: {desvio_padrao}')
    print(f'Coeficiente de Variação: {coef_variacao}')
    print(f'Distância Variância / Média: {distancia_variancia_media}')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose_valor}')

except Exception as e:
    print(f'Erro ao calcular medidas: {e}')


# CARREGAMENTO - LOAD (Não convencional)
# -------------------- VISUALIZAÇÃO --------------------
try:

    print('\nGerando painel gráfico...')

    plt.subplots(2, 2, figsize=(16, 8))
    plt.suptitle('Análise do Bolsa Família por Município')

    # 1 BOX PLOT
    plt.subplot(2, 2, 1)
    plt.boxplot(array_valores, vert=False, showmeans=True) # showfliers=False
    plt.title('Boxplot')

    # 2️ HISTOGRAMA
    plt.subplot(2, 2, 2)
    plt.hist(array_valores, bins=100, edgecolor='black')
    plt.title('Histograma')

    # ---------------------------------------------------------------
    # Printar no terminal as faixas do histograma
    contagens, limites = np.histogram(array_valores, bins=100)
 
    print('\nFaixas do histograma:\n')
    for i in range(len(contagens)):
        print(
            f'Faixa {i+1}: '
            f'R$ {limites[i]:.0f} até R$ {limites[i+1]:.0f} pagos '
            f'=> {contagens[i]} municípios'
        )
    # ---------------------------------------------------------------

    # 3️ BARRAS - OUTLIERS SUPERIORES
    plt.subplot(2, 2, 3)

    df_outliers_plot = (
        df_outliers_superiores
        .sort('VALOR PARCELA', descending=True)   # ordena do maior para o menor
        .head(10)                                 # pega os 10 maiores
        .sort('VALOR PARCELA', descending=False)  # reordena para gráfico horizontal
    )

    plt.barh(
        df_outliers_plot['NOME MUNICÍPIO'],
        df_outliers_plot['VALOR PARCELA']
    )

    plt.title('Outliers Superiores')

    # 4️ MEDIDAS
    plt.subplot(2, 2, 4)

    plt.text(0.0, 0.9, f'Média: {media:,.2f}')
    plt.text(0.0, 0.8, f'Mediana: {mediana:,.2f}')
    plt.text(0.0, 0.7, f'Q1: {q1:,.2f}')
    plt.text(0.0, 0.6, f'Q3: {q3:,.2f}')
    plt.text(0.0, 0.5, f'IQR: {iqr:,.2f}')
    plt.text(0.0, 0.4, f'Mínimo: {minimo:,.2f}')
    plt.text(0.0, 0.3, f'Máximo: {maximo:,.2f}')
    plt.text(0.0, 0.2, f'Amplitude: {amplitude_total:,.2f}')

    plt.text(0.5, 0.9, f'Desvio Padrão: {desvio_padrao:,.2f}')
    plt.text(0.5, 0.8, f'Variância: {variancia:,.2f}')
    plt.text(0.5, 0.7, f'Coef. Variação: {coef_variacao:,.4f}')
    plt.text(0.5, 0.6, f'Assimetria: {assimetria:,.4f}')
    plt.text(0.5, 0.5, f'Curtose: {curtose_valor:,.4f}')

    plt.axis('off')
    plt.tight_layout()

    # Para não influenciar no tempo de fechar o gráfico
    hora_impressao = datetime.now()
    print(f"Tempo de execução: {hora_impressao - hora_import}")

    plt.show()

except Exception as e:
    print("Erro ao gerar gráficos: ", e)


# Salvando os dados
try:
    df_bolsa_familia.write_csv("./dados_salvos/bolsa_familia_processado.csv")
    df_outliers_superiores.write_csv("./dados_salvos/outliers_superiores.csv")
    df_outliers_inferiores.write_csv("./dados_salvos/outliers_inferiores.csv")

    # Salvando as medidas.
    # Transformar em Dataframe e Exportar como csv
    df_metricas = pl.DataFrame({
        "media": [media],
        "mediana": [mediana],
        "q1": [q1],
        "q3": [q3],
        "iqr": [iqr],
        "minimo": [minimo],
        "maximo": [maximo],
        "variancia": [variancia],
        "desvio_padrao": [desvio_padrao],
        "coef_variacao": [coef_variacao],
        "assimetria": [assimetria],
        "curtose": [curtose_valor]
    })

    df_metricas.write_csv("./dados_salvos/metricas_estatisticas.csv")

except Exception as e:
    print("Erro ao gerar gráficos: ", e)