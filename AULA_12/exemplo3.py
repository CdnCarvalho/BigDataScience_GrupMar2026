import pandas as pd
# pip install openpyxl

# Lendo um arquivo Excel com o método read_excel
df = pd.read_excel('./aula_01/vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas da planilha Excel:")
print(df)


# Exibindo o DataFrame atualizado
print("\nDataFrame com bônus e lucro líquido:")
print(df)

# Valor máximo de faturamento total
print("\nMaior valor de faturamento total:")
print(df['Faturamento Total (R$)'].max())

# Valor menor de faturamento
print("\nMenor valor de faturamento:")
print(df['Faturamento Total (R$)'].min())

# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(df['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df['Preço por Unidade (R$)'].mean())


# Criando a coluna de bônus de 6%
df['Pagamento de Bônus (R$)'] = df['Faturamento Total (R$)'] * 0.06

# Criando a coluna de lucro líquido
df['Lucro Líquido (R$)'] = (
    df['Faturamento Total (R$)'] - df['Pagamento de Bônus (R$)']
)


# Produtos com faturamento acima de 30000
print("\nProdutos com faturamento total acima de R$ 30000:")
print(df[df['Faturamento Total (R$)'] > 30000])