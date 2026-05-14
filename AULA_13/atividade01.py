import pandas as pd

# Passo 1: Carregando a planilha de vendas de uma loja de roupas
df_roupas = pd.read_excel('vendas_roupas.xlsx')

# Passo 2: Exibindo as 10 primeiras linhas da planilha
print("\nAs primeiras 10 linhas da planilha:")
print(10 * '=')
print(df_roupas.head(10))


# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(45 * '=')
print(df_roupas['Unidades Vendidas'].sum())


# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(45 * '=')
print(df_roupas['Preço por Unidade (R$)'].mean())


# Maior valor de faturamento total
print("\nMaior valor de faturamento total:")
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].max())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax()])  # Mostra todas as informações da linha do menor valor


# Menor faturamento total
print("\nMenor valor de Faturamento total:")
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].min())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin()])  # Mostra todas as informações da linha do menor valor


# Menor nível de satisfação
print("\nProdutos com menores níveis de satisfação:")
print(120 * '=')
print(df_roupas[df_roupas['Satisfação'] == 'Baixo'])


# Produtos com faturamento acima da média
print("\nProdutos acima da média de faturamento:")
print(120 * '=')
media = df_roupas['Faturamento Total (R$)'].mean()
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'] >= media])

# ------------------------------------ Somente até aqui -----------------------------------------------------------


# agrupando por produto
print("\nAgrupando por produto:")
print(45 * '=')
df_roupas_agrupadas = df_roupas.groupby('Produto', as_index=False)['Faturamento Total (R$)'].sum()
print(df_roupas_agrupadas)


# Ordenando por faturamento
print("\nOrdenando por faturamento:")
print(45 * '=')
df_roupas_agrupadas = df_roupas_agrupadas.sort_values(by='Faturamento Total (R$)', ascending=False)
print(df_roupas_agrupadas)




# ---------------------------------------- Outros Métodos --------------------------
# Mostra Quantas vezes os preços apareceram por produto
print("\nProdutos e preços:")
print(45 * '=')
print(df_roupas[['Produto', 'Preço por Unidade (R$)']].value_counts())

# Quantas vezes cada preço aparece. Não mostra os produtos
print("\nFrequência dos preços:")
print(30 * '=')
print(df_roupas['Preço por Unidade (R$)'].value_counts())


# VALOR DA MODA
# Retorna o número que é a moda usando UM método específico (Mostra o Índice também)
print("\nModa (usando mode):")
print(30 * '=')
print(df_roupas['Preço por Unidade (R$)'].mode())

# Retorna o valor, q é o Preço mais frequente, não mostra o índice. Isto é a (moda)
print("\nModa do preço por unidade:")
print(30 * '=')
print(df_roupas['Preço por Unidade (R$)'].value_counts().index[0])


# QUANTIDADE DE VEZES QUE A MODA APARECE
# Retorna quantas vezes o valor mais frequente aparece.
# Quantidade de vezes que a moda aparece
print("\nFrequência da moda:")
print(30 * '=')
print(df_roupas['Preço por Unidade (R$)'].value_counts().iloc[0])


# Resumo estatístico (média, desvio padrão, quartis, etc.)
print("\nResumo estatístico:")
print(100 * '=')
print(df_roupas.describe())

