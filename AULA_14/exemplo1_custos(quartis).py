# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
import os

os.system('cls')


# Obtendo os dados: 
# ------------------------------------------------------------------------------------------
# Carrega a base de dados a partir do arquivo CSV
df_planilha_custos = pd.read_csv('planilha_de_custos.csv')
print('\nDados Obtidos com sucesso')
print(100 * '-')
print(df_planilha_custos.head())


# Prepara os dados
# ------------------------------------------------------------------------------------------
# Cria a coluna de Custo Total (R$)
# O imposto é calculado diretamente na expressão, sem gerar coluna intermediária
df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] +
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] / 100) +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
)

# Exibe algumas colunas para conferência do cálculo
print('\nDataFrame com a coluna de Custo Total (R$)')
print(50 * '-')
print(df_planilha_custos)
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head())


# Converte a coluna Custo Total em um array NumPy
# ------------------------------------------------------------------------------------------
array_custo_total = np.array(df_planilha_custos['Custo Total (R$)'])


# medidas de tendência central
# ------------------------------------------------------------------------------------------
# Calcula a média
media = np.mean(array_custo_total)

# Calcula a mediana
mediana = np.median(array_custo_total)

# mostrar as medidas de tendência central
print('\nMedidas de Tendência Central')
print(50 * '-')
print(f'Média: R$ {media:.2f}')
print(f'Mediana: R$ {mediana:.2f}') 


# medidas de posição
# ------------------------------------------------------------------------------------------
# Calcula os quartis usando NumPy
q1 = np.quantile(array_custo_total, 0.25)
q2 = np.quantile(array_custo_total, 0.50)  # Mediana
q3 = np.quantile(array_custo_total, 0.75)


# Exibe os resultados
print('\nMedidas de Posição (Quartis)')
print(50 * '-')
print(f'(Q1): {q1:.2f}')  # 25% dos produtos têm custo total até R$ 1.667,77
print(f'(Q2): {q2:.2f}')  # Metade dos produtos custa até R$ 3.133,31
print(f'(Q3): {q3:.2f}')  # 75% dos produtos custam até R$ 4.479,05

