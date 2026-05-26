# EXEMPLO 2 - Utilizando Pandas sem função
import pandas as pd
from sqlalchemy import create_engine


# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'mod2_aula3'


# Cria a conexão com o banco
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)


# Query SQL
query = "SELECT * FROM materiais_construcao"


# query = """
# SELECT * FROM materiais_construcao
# WHERE fornecedor = 'local';
# """

# query = """
# SELECT * FROM materiais_construcao
# WHERE preco > 490;
# """

# query = """
# SELECT * FROM materiais_construcao
# WHERE categoria = 'hidraulica'
# AND preco < 185;
# """

# query = """
# SELECT * FROM materiais_construcao
# WHERE categoria = 'alvenaria'
# AND (fornecedor = 'olaria' OR fornecedor = 'precon');
# """

# Lê os dados da tabela e transforma em DataFrame
df_materiais = pd.read_sql(query, engine)

# Exibe o DataFrame completo
print(df_materiais)