# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np


# Obtendo os dados: Carrega a base de dados a partir do arquivo CSV
# ------------------------------------------------------------------------------------------
df_planilha_moveis = pd.read_csv('planilha_moveis.csv')

# Exibe as primeiras linhas para conferência dos dados
print('\nDados Obtidos com sucesso')
print(100 * '-')
print(df_planilha_moveis.head())


# Cria a coluna de Total de Vendas (R$)
# Total de Vendas = quantidade vendida × preço do produto
df_planilha_moveis['Total de Vendas (R$)'] = (
    df_planilha_moveis['Vendidos'] * df_planilha_moveis['Preco']
)


# Exibe algumas colunas para conferência do cálculo
print('\nTotal de Vendas (R$) calculado')
print(100 * '-')
print(df_planilha_moveis)

print('\nApenas as colunas Produto e Total de Vendas (R$)')
print(50 * '-')
print(df_planilha_moveis[['Produto', 'Total de Vendas (R$)']])


# -----------------------------------------------------------------------------------------------
# Converte a coluna Total de Vendas em um array NumPy
array_total_vendas = np.array(df_planilha_moveis['Total de Vendas (R$)'])


# Medidas de tendência central
# Calcula a média
media = np.mean(array_total_vendas)

# Calcula a mediana 
mediana = np.median(array_total_vendas)

print('\nMedidas de tendência central')
print(30 * '-')
print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')


# Medidas de Posição
# Calcula os quartis usando NumPy
q1 = np.quantile(array_total_vendas, 0.25)
q2 = np.quantile(array_total_vendas, 0.50)  # Mediana
q3 = np.quantile(array_total_vendas, 0.75)

# Exibe os resultados
print('\nMedidas de posição')
print(30 * '-')
print(f'Q1: {q1:.2f}')
print(f'Q2: {q2:.2f}')
print(f'Q3: {q3:.2f}')


