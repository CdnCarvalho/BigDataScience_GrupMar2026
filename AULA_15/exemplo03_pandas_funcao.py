# EXEMPLO - Conexão com banco utilizando função
import pandas as pd
from sqlalchemy import create_engine


# FUNÇÃO DE CONEXÃO - A função recebe os dados para criar a conexão com o banco
def conectar_banco(host, user, password, database):

    # Cria a engine de conexão
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{database}'
    )

    # Retorna a conexão criada
    return engine


# Evita notação científica
# Configura os separadores de milhar e decimal
pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.float_format', '{:,.2f}'.format)


# VARIÁVEIS DE CONEXÃO
host = 'localhost'
user = 'root'
password = '123456'
database = 'mod2_aula3'


# CHAMANDO A FUNÇÃO
engine = conectar_banco(host, user, password, database)


# QUERY SQL
# P/ selecionar todos os dados da tabela
query = "SELECT * FROM cadastro_produtos"

# query = """
# SELECT * FROM cadastro_produtos
# WHERE categoria = 'Informática';
# """


# LENDO OS DADOS COM PANDAS
# Usa a query e a engine para ler os dados do banco
df_produtos = pd.read_sql(query, engine)


# EXIBINDO O DATAFRAME COMPLETO
print(df_produtos)


# CRIA A SÉRIE TOTAL -  Multiplica o preço pela quantidade vendida
df_produtos['total'] = (
    df_produtos['Preço Unitario'] * df_produtos['Custo Unitario']
)


# AGRUPANDO POR PRODUTO - Soma o total de vendas de cada produto
df_produtos_ag = (
    df_produtos
    .groupby('Produto', as_index=False)['total']
    .sum()
)


# ORDENANDO DO MAIOR PARA O MENOR 
# reset_index = reorganiza os índices
# drop=True = evita que o índice antigo vire coluna
df_produtos_ag = (
    df_produtos_ag
    .sort_values(by='total', ascending=False)
    .reset_index(drop=True)
)


# EXIBINDO O RESULTADO FINAL
print(df_produtos_ag)