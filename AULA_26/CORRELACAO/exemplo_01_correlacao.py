import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter dados
try:
    print('Obtendo dados...')
    
    # Diretamente do arquivo
    # df_ocorrecias = pd.read_csv('BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='iso-8859-1')
    
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo','recuperacao_veiculos']]

    # Agrupar e totalizar os roubos e recuperações por CISP no pandas novo   
    df_total_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()

    print(df_total_veiculos.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# Correlação
try:
    print('Calculando a correlação...')

    # Correlação de Pearson
    correlacao = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])[0,1]
    print(f'Correlação: {correlacao}')

    # plotar gráfico
    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Roubo de Veículos')
    plt.ylabel('Recuperação de Veículos')

    plt.show()

except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()