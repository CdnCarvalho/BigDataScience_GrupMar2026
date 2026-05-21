# EXEMPLO 2 - Utilizando Pandas com função
import pandas as pd
from sqlalchemy import create_engine


# FUNÇÃO DE CONEXÃO
def conectar_banco(host, user, password, database):

    # Cria a conexão com o banco
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{database}'
    )

    # Retorna a conexão criada
    return engine


# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'mod2_aula3'


# Chamando a função
engine = conectar_banco(host, user, password, database)

query = "SELECT * FROM materiais_construcao";

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
df_materiais_construcao = pd.read_sql(query, engine)


# Exibe o DataFrame completo
print(df_materiais_construcao)

# # cria a série total
df_materiais_construcao['total'] = (
    df_materiais_construcao['preco'] * df_materiais_construcao['quantidade_vendida']
)


# # agrupando por produto
df_materiais = df_materiais_construcao.groupby('produto', as_index=False)['total'].sum()


# # ordenando pelo preço do maior para o menor
# # drop true p/ evitar q index vire nova coluna
# # reset_index = p/ numerar novamente
df_materiais = df_materiais.sort_values(by='total', ascending=False).reset_index(drop=True)
print(df_materiais)
