# ATIVIDADE
# Mostre o nome do cliente, a data do pedido e o nome de cada produto comprado e a data.

# Instalação (se ainda não tiver instalado)
# pip install sqlalchemy pymysql pandas

from sqlalchemy import create_engine
import pandas as pd

# Configurações do banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'abril2025_mod02_pedido'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Conexão com o banco de dados
try:
    # Lê as tabelas diretamente do MySQL
    df_clientes = pd.read_sql('tb_clientes', con=engine)
    df_pedidos = pd.read_sql('tb_pedidos', con=engine)

except Exception as e:
    print(f'Erro ao conectar ao banco: {e}')
    # df_clientes = pd.DataFrame()
    # df_pedidos = pd.DataFrame()

# Lê os arquivos CSV (itens e produtos)
df_itens = pd.read_csv('tb_itens.csv')
df_produtos = pd.read_csv('tb_produtos.csv')

# JOIN: pedidos + clientes
df_base = pd.merge(df_pedidos, df_clientes, left_on='cliente_codigo', right_on='cod_cliente')

# JOIN: adiciona os itens do pedido
df_base = pd.merge(df_base, df_itens, left_on='codigo_pedido', right_on='pedido_codigo')

# JOIN: adiciona os dados do produto
df_base = pd.merge(df_base, df_produtos, left_on='item_codigo', right_on='codigo_produto')

# Exibe nome do cliente, data do pedido e nome do produto
print(df_base[['nome', 'data_pedido', 'produto']])
