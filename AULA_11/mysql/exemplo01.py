import pandas

dados = {
    'cargos': ["assistente", "auxiliar", "gerente"],
    'salários': [2500, 1800, 7500]
}


df_dados = pandas.DataFrame(dados)
print(df_dados) 

print(df_dados['salários']) # salárioos
print(df_dados['cargos']) # cargos

# maior valor, menor valor, média e total
print(df_dados['salários'].max())
print(df_dados['salários'].min())
print(df_dados['salários'].mean())
print(df_dados['salários'].sum())


# exportar para csv
df_dados.to_csv('base2.csv', index=False)

# Atividade: base do Kaggle.com : 
# https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data

# Lendo CSV
# df_csv = pandas.read_csv('./mysql/base1.csv')
# df_csv = pandas.read_csv('./mysql/loja_roupas.csv')
# print(df_csv)