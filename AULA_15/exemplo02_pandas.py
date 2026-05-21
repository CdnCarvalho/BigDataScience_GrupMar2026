# EXEMPLO 2 - Utilizando Pandas com SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine


# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'mod2_aula3'


# URL de conexão com o banco
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

# Query SQL
query = "SELECT * FROM cadastro_produtos"

# Lê os dados do banco e transforma em DataFrame
df_produtos = pd.read_sql(query, engine)

# Exibe o DataFrame completo
print(df_produtos)
