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


# Medidas de Dispersão
try:
    print('Calculando medidas de dispersão...')

    # Variância
    # É uma medida para obsersar a dispersão dos dados 
    # Observa-se em relação a média
    # É a média dos quadrados das diferenças entre cada valor e a média
    # O resultado da variância etá elevado ao quadrado

    # Interpretação
    # Quanto maior a variância, maior é o afastamento dos valores em relação à média.
    # Neste caso, a variância elevada indica alta dispersão dos dados.
    variancia = np.var(array_roubo_veiculo)


    # Distância da variância para a média
        # Distância <= |10%| : Baixa dispersão dos dados em relação a média
        # Distância > |10%| e distância < |25%|: Dispersão moderada dos dados em relação a média
        # Distâcia >= |25%|: Alta dispersão dos dados em relação a média
    distancia_var_media = variancia / (media_roubo_veiculo ** 2)

    # Desvio padrão é a raiz quadrada da variância
    # Desvio padrão é a normalização da variância, por isso mais fácil de interpretar
    # Apresentar o quanto os dados estão afastados da média (para mais ou para menos). Valor absoluto
    desvio_padrao = np.std(array_roubo_veiculo)

    # Coeficiente de variação
    # É a magnitude do desvio padrão em realção a média
    coef_variacao = desvio_padrao / media_roubo_veiculo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Dist. var x média: {distancia_var_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coef. variação: {coef_variacao}')

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')
    exit()


# Medidas de distribuição
try:
    print('Calculando medidas de distribuição...')

    # Assimetria (Skewness)
    # Assimetria é uma medida que indica como os dados estão distribuídos em torno do valor central.
    #
    # Os valores estão equilibrados em torno do centro?
    # Existe uma quantidade maior de registros com valores menores ou maiores?
    # O "peso" da distribuição está mais para os valores menores ou para os valores maiores?
    #
    # É uma medida utilizada para descrever o grau de simetria ou assimetria de uma distribuição.
    #
    # Escala de interpretação:
    #
    # Assimetria > 1.0
    # Assimetria positiva alta.
    # A cauda é longa à direita.
    # Existem alguns valores muito altos puxando a média para cima.
    # A média tende a ser maior que a mediana.
    #
    # Assimetria entre 0.5 e 1.0
    # Assimetria positiva moderada.
    # A cauda à direita está presente, mas é menos acentuada.
    #
    # Assimetria entre -0.5 e 0.5
    # Distribuição aproximadamente simétrica.
    # Os dados tendem a estar equilibrados em torno do centro.
    # A média e a mediana tendem a ter valores próximos.
    #
    # Assimetria entre -1.0 e -0.5
    # Assimetria negativa moderada.
    # A cauda à esquerda está presente, mas é menos acentuada.
    #
    # Assimetria < -1.0
    # Assimetria negativa alta.
    # A cauda é longa à esquerda.
    # Existem alguns valores muito baixos puxando a média para baixo.
    # A média tende a ser menor que a mediana.
    assimetria = df_roubo_veiculo['roubo_veiculo'].skew()

    # curtpse. Kurtosis
    # é uma medida que descreve o formato da distribuição dos dados. 
    # Nos ajuda a entender se os valores estão mais concentrados próximos da média 
    # ou mais espalhados pela distribuição.
    # Pode indicar a presença de valores extremos (outliers). 
    # Curtose é alta, geralmente temos muitos valores próximos da média e alguns
    # poucos valores muito distantes dela. 
    # Quando a curtose é baixa, os dados tendem a estar mais distribuídos ao longo da distribuição.
    
    # Curtose ≈ 0 (mesocúrtica)
    # Distribuição “normal”
    # Concentração moderada no centro
    # Poucos extremos relevantes

    # Curtose > 0 (leptocúrtica)
    # Pico mais alto
    # Muitos valores próximos da média
    # Outliers mais fortes
    # Caudas mais “pesadas”

    # Curtose < 0 (platicúrtica)
    # Pico achatado
    # Dados mais espalhados
    # Poucos extremos
    # Distribuição mais uniforme
    curtose = df_roubo_veiculo['roubo_veiculo'].kurtosis()

    print('\nMedidas de distribuição: ')
    print(30*'-')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')

    # Simetria:
    # Indica se os dados estão equilibrados em torno do centro ou se 
    # há predominância de valores em um dos lados da distribuição.
    # Curtose:
    # Indica o grau de concentração dos dados em torno da média e
    # a presença de valores extremos.


except Exception as e:
    print(f'Erro ao calcular as medidas de distribuição: {e}')
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

    plt.barh(df_roubo_veiculo_maiores['munic'], df_roubo_veiculo_maiores['roubo_veiculo'])

    plt.title('Top 10 - Municípios com maiores roubos')


    # ===================================================
    # POSIÇÃO 2 - HISTOGRMA
    # ===================================================
    plt.subplot(2, 2, 2)

    plt.hist(array_roubo_veiculo, bins=198, edgecolor='black')
    plt.axvline(media_roubo_veiculo, color='green', linewidth=1)
    plt.axvline(mediana_roubo_veiculo, color='orange', linewidth=1)

    # Printar no terminal as faixas do histograma
    contagens, limites = np.histogram(array_roubo_veiculo, bins=158)

    print('\nFaixas do histograma:\n')
    for i in range(len(contagens)):

        if contagens[i] > 0:
            print(
                f'Faixa {i+1}: '
                f'{limites[i]:.0f} até {limites[i+1]:.0f} roubos '
                f'=> {contagens[i]} municípios'
            )

    # A curtose está indicando que existem municípios extremamente diferentes da 
    # maioria dos municípios.
    # A maior parte dos municípios possui poucos roubos, mas alguns municípios 
    # apresentam quantidades muito superiores ao padrão geral dos dados.

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

    plt.text(0.1, 0.9, f'Média: {media_roubo_veiculo}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana_roubo_veiculo}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12)
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)

    plt.text(0.6, 0.9, f'Assimetria: {assimetria}', fontsize=12)
    plt.text(0.6, 0.8, f'Curtose: {curtose}', fontsize=12)
    plt.text(0.6, 0.7, f'Variancia: {variancia}', fontsize=12)
    plt.text(0.6, 0.6, f'Desvio Padrão: {desvio_padrao}', fontsize=12)
    plt.text(0.6, 0.5, f'Coeficiente de Variação: {coef_variacao}', fontsize=12)

    plt.axis('off')
    plt.title('Resumo Estatístico')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()