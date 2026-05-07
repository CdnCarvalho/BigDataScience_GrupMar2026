# pip install pandas sqlalchemy pymysql
#  ou assim:   python -m pip install pandas sqlalchemy pymysql

# Problema com scripts:
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_aula11'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df = pd.read_sql('tb_produtos', engine)

print(df.head())
print(df['produto'])

# maior valor
print(df['preco'].max())

# menor valor
print(df['preco'].min())

# média arredondada
print(df['preco'].mean())
print(round(df['preco'].mean(), 2))

# Coluna do total arrecadado
df['total'] = df['preco'] * df['vendidos']

# mostrar os totais e os produtos
print(df[['produto', 'total']])

# Total geral
print(f'Arrecadação total: {df["total"].sum()}')


