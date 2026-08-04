# Importar as bibliotecas
import pandas as pd 
import numpy as np

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obtendo dados
try:

    df_roubos = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    print(df_roubos['regiao'].unique())  # testar as impressões
    print(df_roubos.head())

except Exception as e:
    print("Erro ao obter dados do ISP: ", e)


# Tratando e preparando os dados
try:
    # Delimitando as variáveis
    df_roubos = df_roubos[['cisp', 'regiao', 'munic', 'roubo_veiculo']]
    # print(df_roubos.head())
    
    # Verifica 'regiao' se os valores começam com 'Grande Niter'
    # O parâmetro na=False evita erro caso existam valores vazios (NaN)
    correcao_acentuacao = df_roubos['regiao'].str.startswith('Grande Niter', na=False)
    # print(correcao_acentuacao)

    # Substituir os dados em todas as linhas onde a condição for verdadeira em regiao
    df_roubos.loc[correcao_acentuacao, 'regiao'] = 'Grande Niterói'
    print(df_roubos['regiao'].unique())  # Imprimir apenas valores únicos da série região

    # Agrupando os dados por cisp, região e município
    df_roubos = df_roubos.groupby(['cisp', 'regiao', 'munic'], as_index=False)['roubo_veiculo'].sum()

    # display(df_roubos)  # é uma função do Jupyter Notebook que permite exibir o DataFrame
    
except Exception as e:
    print("Erro no tratamento dos dados: ", e)


# Calculando as medidas
try:
    array_roubos = np.array(df_roubos['roubo_veiculo'])
    # print(array_roubos)
    
    media = np.mean(array_roubos)
    mediana = np.median(array_roubos)
    total = np.sum(array_roubos)
    # maximo = np.max(array_roubos)
    # minimo = np.min(array_roubos)

    # Obtendo os Quartis
    q1 = np.quantile(array_roubos, 0.25)
    q3 = np.quantile(array_roubos, 0.75)

    # Printando as medidas
    print('Medidas:')
    print(f'Media: {media:.2f}')
    print(f'Mediana: {mediana}')
    print(f'Total: {total}')

except Exception as e:
    print("Erro ao obter as medidas: ", e)


# Identificando os maiores e menores
try:

    print('Criando os dataframes dos maiores e menores...')

    # MAIORES
    # O .copy() é importante para evitar problemas ao alterar esse novo DataFrame
    df_maiores = df_roubos[df_roubos['roubo_veiculo'] > q3].copy()

    # Criamos uma nova coluna chamada 'flag' 
    df_maiores['flag'] = 'mais'


    # MENORES
    df_menores = df_roubos[df_roubos['roubo_veiculo'] < q1].copy()

    # Criamos uma coluna no dataframe df_menores 
    df_menores['flag'] = 'menos'

    # juntamos (concatenamos) os dois DataFrames.
    # ignore_index=True reorganiza o índice (0, 1, 2...) após a junção
    df_roubos_flags = pd.concat([df_maiores, df_menores], ignore_index=True)
    print(df_roubos_flags)

except Exception as e:
    print("Erro ao identificar os maiores e menores: ", e)


# Exportando dados csv ou xlsx
try:
    print('Exportando os dataframes...')

    # Testar sem encoding | Impirmir com o encoding utf-8-sig, se precisar do csv fora do BI
    df_roubos_flags.to_csv('roubos_veiculos.csv', index=False)
    
    df_roubos_flags.to_excel('roubos_veiculos.xlsx', index=False)
    print('Datafremes exportados com sucesso!')

except Exception as e:
    print("Erro ao exportar os dados: ", e)
