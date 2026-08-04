# Bibliotecas
import pandas as pd 
import numpy as np

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obtendo dados
try:
    df_drogas = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_drogas['munic'].unique()) | print(df_drogas['regiao'].unique()) 
    print(df_drogas.head())
except Exception as e:
    print("Erro ao obter dados do ISP: ", e)


# Tratando
try:
    # Delimitando as variáveis
    df_drogas = df_drogas[['cisp', 'regiao', 'munic', 'apreensao_drogas']]
    # print(df_drogas.head())
    
    # Tratando os erros de acentuação
    correcao_acentuacao = df_drogas['regiao'].str.startswith('Grande Niter', na=False)

    df_drogas.loc[correcao_acentuacao, 'regiao'] = 'Grande Niterói'
    # print(df_drogas['regiao'].unique())

    # Agrupando os dados cisp, região e município
    # df_drogas = df_drogas.groupby(['cisp', 'regiao', 'munic']).sum(['apreensao_drogas']).reset_index()
    df_drogas = df_drogas.groupby('cisp', as_index=False)['apreensao_drogas'].sum()
    

    # Display() é uma função do Jupyter Notebook que permite exibir o DataFrame
    display(df_drogas)
except Exception as e:
    print("Erro no tratamento dos dados: ", e)


# Calculando as medidas
try:
    array_drogas = np.array(df_drogas['apreensao_drogas'])
    # print(array_drogas)
    
    media = np.mean(array_drogas)
    mediana = np.median(array_drogas)
    total = np.sum(array_drogas)
    # maximo = np.max(array_drogas)
    # minimo = np.min(array_drogas)

    # Obtendo os Quartis
    q1 = np.quantile(array_drogas, 0.25)
    q3 = np.quantile(array_drogas, 0.75)

    # Printando as medidas
    print('Medidas:')
    print(f'Media: {media:.2f}')
    print(f'Mediana: {mediana}')
    print(f'Total: {total}')

except Exception as e:
    print("Erro ao obter as medidas: ", e)


# Identificando os maiores e menores
try:
    # Gerar um dataframe com os maiores
    # Copy() quando preciar alterar um dataframe já filtrado
    df_maiores =  df_drogas[df_drogas['apreensao_drogas'] > q3].copy()
    df_maiores['flag'] = 'mais'
    # print(df_maiores)

    # Gerar um dataframe com os menores
    df_menores = df_drogas[df_drogas['apreensao_drogas'] < q1].copy()
    df_menores['flag'] = 'menos'
    # print(df_menores)

    # Concatenar os dois dataframes
    df_drogas_flags = pd.concat([df_maiores, df_menores], ignore_index=True)

    display(df_drogas_flags)
except Exception as e:
    print("Erro ao identificar os maiores e menores: ", e)



# Exportando dados csv ou xlsx
try:
    # Testar sem encoding | Impirmir com o encoding utf-8-sig, se precisar do csv fora do BI
    df_drogas_flags.to_csv('apreensao_drogas.csv', index=False, )

    df_drogas_flags.to_excel('drogas_veiculos.xlsx', index=False)

except Exception as e:
    print("Erro ao exportar os dados: ", e)