import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis
    df_recup_veiculo = df_ocorrencias[['cisp', 'recuperacao_veiculos']]

    # Totalizar
    # df_recup_veiculo = df_recup_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()
    df_recup_veiculo = df_recup_veiculo.groupby(['cisp'], as_index=False)['recuperacao_veiculos'].sum()  # Versão mais nova do pandas

    print(df_recup_veiculo.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# descrever a distribuição dos dados
try:
    print('Descrevendo a distribuição dos dados...')

    # Converter para um array numpy
    array_recup_veiculo = np.array(df_recup_veiculo['recuperacao_veiculos'])

    # Medidas de tendência central
    media = np.mean(array_recup_veiculo)
    mediana = np.median(array_recup_veiculo)
    distancia_media_mediana = (media-mediana)/mediana



    # Medidas de posição e dipersão - quartil
    q1 = np.quantile(array_recup_veiculo, 0.25, method='weibull')
    q3 = np.quantile(array_recup_veiculo, 0.75, method='weibull')
    


    # IQR
    iqr = q3 - q1
    limite_inferior = q1 - (1.5*iqr)
    limite_superior = q3 + (1.5*iqr)



    # Medidas de posição e dispersão
    minimo = np.min(array_recup_veiculo)
    maximo = np.max(array_recup_veiculo)
    amplitude_total = maximo - minimo

    print('\nMedidas de Tendência Central')
    print(30*'-')
    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Distância média da mediana: {distancia_media_mediana:.2f}')

    print('\nMedidas de Posição e Dispersão')
    print(30*'-')
    print(f'Menor valor: {minimo}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q3: {q3}')
    print(f'Limite superior: {limite_superior}')
    print(f'Maior valor: {maximo}')
    print(f'IQR: {iqr}')
    print(f'Amplitude total: {amplitude_total}')



    # OUTLIERS SUPERIORES 
    df_recup_veiculo_outliers_sup = df_recup_veiculo[df_recup_veiculo['recuperacao_veiculos'] > limite_superior].copy()

    print('\nDPs com recuperações superiores as demais:')
    print(30*'-')
    if len(df_recup_veiculo_outliers_sup) == 0:
        print('Não existem DPs com valores discrepantes supreiores')
    else:
        print(df_recup_veiculo_outliers_sup.sort_values(by='recuperacao_veiculos', ascending=False))



    # OUTLIERS INFERIORES
    df_recup_veiculo_outliers_inf = df_recup_veiculo[df_recup_veiculo['recuperacao_veiculos'] < limite_inferior].copy()

    print('\nDPs com recuperações inferiores as demais:')
    print(30*'-')
    if len(df_recup_veiculo_outliers_inf) == 0:
        print('Não existem DPs com valores discrepantes inferiores')
    else:
        print(df_recup_veiculo_outliers_inf.sort_values(by='recuperacao_veiculos', ascending=True))

   
    # DPs QUE MENOS RECUPERARAM VEÍCULOS 
    df_recup_veiculo_q1 = df_recup_veiculo[df_recup_veiculo['recuperacao_veiculos'] < q1]

    print('\nDPs que menos recuperaram veículos:')
    print(30*'-')
    print(df_recup_veiculo_q1.sort_values(by='recuperacao_veiculos', ascending=True))

except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
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
    variancia = np.var(array_recup_veiculo)


    # Distância da variância para a média
        # Distância <= |10%| : Baixa dispersão dos dados em relação a média
        # Distância > |10%| e distância < |25%|: Dispersão moderada dos dados em relação a média
        # Distâcia >= |25%|: Alta dispersão dos dados em relação a média
    distancia_var_media = variancia / (media ** 2)

    # Desvio padrão é a raiz quadrada da variância
    # Desvio padrão é a normalização da variância, por isso mais fácil de interpretar
    # Apresentar o quanto os dados estão afastados da média (para mais ou para menos). Valor absoluto
    desvio_padrao = np.std(array_recup_veiculo)

    # Coeficiente de variação
    # É a magnitude do desvio padrão em realção a média
    coef_variacao = desvio_padrao / media

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Dist. var x média: {distancia_var_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coef. variação: {coef_variacao}')

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')
    exit()



# visualizar os dados
try:
    print('Visualizando os dados...')

    plt.subplots(1,3, figsize=(18,6))
    plt.suptitle('Análise da recuperação de veículos por DP (CISP)')



    # --- SUBPLOT 1: Boxplot com outliers
    plt.subplot(1,3,1)
    plt.boxplot(array_recup_veiculo, vert=False, showmeans=True)
    plt.title('Boxplot com outliers')



    # --- SUBPLOT 2: DPs com maiores recuperações (outliers superiores)
    plt.subplot(1,3,2)       
    df_recup_veiculo_outliers_sup['cisp'] = (
        df_recup_veiculo_outliers_sup['cisp'].astype(str) # converter CISP para string
    )  
    
    # Ordenando
    df_recup_veiculo_outliers_sup = (
        df_recup_veiculo_outliers_sup
        .sort_values(by='recuperacao_veiculos', ascending=True)
)
    plt.barh(df_recup_veiculo_outliers_sup['cisp'], df_recup_veiculo_outliers_sup['recuperacao_veiculos'])
   
    # TOP 5
    # df_top5 = (
    #     df_recup_veiculo_outliers_sup
    #         .sort_values(by='recuperacao_veiculos', ascending=False)
    #         .head(5)
    #         .sort_values(by='recuperacao_veiculos', ascending=True)
    # )
    
    # plt.barh(df_top5['cisp'], df_top5['recuperacao_veiculos'])

    plt.title('Maiores recuperações')



    # --- SUBPLOT 3: Medidas descritivas
    plt.subplot(1,3,3)

    plt.text(0.05, 0.9, f'Média: {media}', fontsize=11)
    plt.text(0.05, 0.8, f'Mediana: {mediana}', fontsize=11)
    plt.text(0.05, 0.7, f'Distância: {distancia_media_mediana:.2f}', fontsize=11)
    plt.text(0.05, 0.6, f'Mínimo: {minimo}', fontsize=11)
    plt.text(0.05, 0.5, f'Q1: {q1}', fontsize=11)
    plt.text(0.05, 0.4, f'Q3: {q3}', fontsize=11)
    plt.text(0.05, 0.3, f'IQR: {iqr}', fontsize=11)
    plt.text(0.05, 0.2, f'Máximo: {maximo}', fontsize=11)
    plt.text(0.05, 0.1, f'Amplitude: {amplitude_total}', fontsize=11)

    # Desvio padrão, distância, coeficiente de variação e variância
    plt.text(0.6, 0.9, f'Desvio Padrão: {desvio_padrao}', fontsize=12)
    plt.text(0.6, 0.8, f'Variância: {variancia}', fontsize=12)
    plt.text(0.6, 0.7, f'Coeficiente de Variação: {coef_variacao}', fontsize=12)
    plt.text(0.6, 0.6, f'Dist. Var x Média: {distancia_var_media}', fontsize=12)

    # Medidas de dispersão

    plt.axis('off')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Erro ao visualizar os dados: {e}')
    exit()