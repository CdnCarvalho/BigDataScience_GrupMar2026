# # ATIVIDADE
# --------------------------------------------------------------------------------
# # Mostre o nome do cliente e a data de cada pedido realizado.

# # Instalação (se ainda não tiver instalado)
# # pip install sqlalchemy pymysql pandas
from sqlalchemy import create_engine
import pandas as pd

# Configurações do banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_atividade_pedidos_aula02'

# Cria o engine (conexão)
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

try:
    # Consulta SQL com JOIN
    query = """
    SELECT 
        p.codigo_pedido,
        c.nome,
        c.cidade,
        p.data_pedido,
        p.valor
    FROM tb_pedidos p
    INNER JOIN clientes c
        ON p.cliente_codigo = c.codigo_cliente
    """
    # Leitura das tabelas diretamente para DataFrames
    df_relacionado = pd.read_sql(query, con=engine)
    print('\nPROCESSAMENTO NO BANCO - JOIN:')
    print(df_relacionado)

except Exception as e:
    print(f'Erro ao conectar ou consultar o banco: {e}')


# Limpeza e padronização dos dados
try:
    # DataFrame Ordenado por data do pedido decrescente
    df_ordenado = df_relacionado.sort_values(by='data_pedido', ascending=False)
    print('\nOrdenado por Data (Decrescente):')
    print(df_ordenado)

    # Separar por Categoria - Exemplo: Cidade Curitiba
    df_curitiba = df_relacionado[df_relacionado['cidade'] == 'Curitiba']
    print('\nDataFrame - Cidade de Curitiba:')
    print(df_curitiba)

    # Obtendo os dados onde a cidade é 'Curitiba' ou 'São Paulo'
    df_filtrado_sp_coritiba = df_relacionado[
        (df_relacionado['cidade'] == 'Curitiba') |
        (df_relacionado['cidade'] == 'Sao Paulo')
    ]

    print('\nDataFrame Curitiba ou São Paulo:')
    print(df_filtrado_sp_coritiba)

except Exception as e:
    print(f'Erro na padronização as informações: {e}')