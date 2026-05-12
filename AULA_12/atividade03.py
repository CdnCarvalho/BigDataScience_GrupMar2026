import pandas as pd

# Passo 1: Carregando a planilha de vendas de uma loja de roupas
df_roupas = pd.read_excel('./aula_01/vendas_roupas.xlsx')

# Passo 2: Exibindo as 10 primeiras linhas da planilha
print("\nAs primeiras 10 linhas da planilha:")
print(df_roupas.head(30))



# Exibindo o DataFrame atualizado
print("\nDataFrame com bônus e lucro líquido:")
print(df_roupas)

# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(df_roupas['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df_roupas['Preço por Unidade (R$)'].mean())

# Maior valor de faturamento total
print("\nMaior valor de faturamento total:")
print(df_roupas['Faturamento Total (R$)'].max())

# Menor faturamento total
print("\nMenor valor de faturamento total:")
print(df_roupas['Faturamento Total (R$)'].min())


# Criando a coluna de bônus de 6%
df_roupas['Pagamento de Bônus (R$)'] = (
    df_roupas['Faturamento Total (R$)'] * 0.06
)

# Criando a coluna de lucro líquido
df_roupas['Lucro Líquido (R$)'] = (
    df_roupas['Faturamento Total (R$)']
    - df_roupas['Pagamento de Bônus (R$)']
)

# Produtos com menores níveis de satisfação
print("\nProdutos com menores níveis de satisfação:")
print(df_roupas[df_roupas['Satisfação'] == 'Baixo'])