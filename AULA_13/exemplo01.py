import pandas as pd

# Lendo um arquivo Excel com o método read_excel (deve apontar para o arquivo real)
df_eletronicos = pd.read_excel('vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("\nPrimeiras linhas dos dados:")
print(120 * "=")
print(df_eletronicos.head(30))


# Valor máximo de faturamento total
print("\nMaior valor de faturamento total:")
print(45 * "=")
print(df_eletronicos['Faturamento Total (R$)'].max())
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax(), 'Produto'])  # Mostra apenas o nome do produto de maior valor
# print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax()])  # Mostra todas as informações da linha do maior valor (Muito Útil)


# Valor menor de faturamento
print("\nMenor valor de faturamento:")
print(45 * "=")
print(df_eletronicos['Faturamento Total (R$)'].min())
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmin(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
# print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmin()])  # Mostra todas as informações da linha do menor valor (Muito Útil)


# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(45 * "=")
print(df_eletronicos['Preço por Unidade (R$)'].mean())



# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(45 * "=")
print(df_eletronicos['Unidades Vendidas'].sum())



# Produtos com faturamento acima da média
print("\nProdutos acima da média:")
print(120 * "=")
media = df_eletronicos['Faturamento Total (R$)'].mean()
print(df_eletronicos[df_eletronicos['Faturamento Total (R$)'] >= media])
#  ------------------------------------------ somente até aqui -------------------------------------------



# Delimitando as colunas e agrupando por produto
print("\nFaturamento total por produto (Produtos Agrupados):")
print(45*"=")
df_produtos = df_eletronicos[['Produto', 'Faturamento Total (R$)']]
df_produtos = df_produtos.groupby('Produto', as_index=False)['Faturamento Total (R$)'].sum()
print(df_produtos)


# Ordenando do maior para o menor (decrescente)
print("\nFaturamento Ordenado:")
print(45*"=")
df_produtos = df_produtos.sort_values(by='Faturamento Total (R$)', ascending=False)
print(df_produtos.sort_values(by='Faturamento Total (R$)', ascending=True))



# --------------- ------------- Outros Métodos ------------ -------------------
# --------------- ------------- Outros Métodos ------------ -------------------


# Mostra Quantas vezes os preços apareceram por produto
print("\nProdutos e preços:")
print(45 * '=')
print(df_eletronicos[['Produto', 'Preço por Unidade (R$)']].value_counts())


# Quantas vezes cada preço aparece. Não mostra os produtos
print("\nFrequência dos preços:")
print(30 * '=')
print(df_eletronicos['Preço por Unidade (R$)'].value_counts())
# print(df_eletronicos[df_eletronicos['Preço por Unidade (R$)'] == 1500])  # se um aluno perguntar.


# VALOR DA MODA
# Retorna o número que é a moda usando UM método específico (Mostra o Índice também)
print("\nModa (usando mode):")
print(30 * '=')
print(df_eletronicos['Preço por Unidade (R$)'].mode())


# Retorna o valor, q é o preço mais frequente, não mostra o índice. Isto é a (moda)
print("\nModa do preço por unidade:")
print(30 * '=')
print(df_eletronicos['Preço por Unidade (R$)'].value_counts().index[0])


# QUANTIDADE DE VEZES QUE A MODA APARECE
# Retorna quantas vezes o valor mais frequente aparece.
# Quantidade de vezes que a moda aparece
print("\nFrequência da moda:")
print(30 * '=')
print(df_eletronicos['Preço por Unidade (R$)'].value_counts().iloc[0])


# Resumo estatístico (média, desvio padrão, quartis, etc.)
print("\nResumo estatístico:")
print(100 * '=')
print(df_eletronicos.describe())
