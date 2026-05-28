# Liste os pedidos feitos por clientes que moram em São Paulo.
# pip install sqlalchemy pymysql pandas
from sqlalchemy import create_engine
import pandas as pd


# Configurações do banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_vendas'


# Cria o engine (conexão)
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)


# LEITURA DAS TABELAS
try:

    # Tabela de clientes
    df_clientes = pd.read_sql('tb_clientes', con=engine)

    # Tabela de pedidos
    df_pedidos = pd.read_sql('tb_pedidos', con=engine)

    # Tabela de itens do pedido
    df_itens = pd.read_sql('tb_itens', con=engine)

    # Tabela de produtos
    df_produtos = pd.read_sql('tb_produtos', con=engine)


    # =========================================================================
    # RENOMEANDO COLUNAS
    # Para que os merges possam usar apenas ON
    # =========================================================================

    # cliente_codigo => codigo_cliente
    df_pedidos = df_pedidos.rename(
        columns={'cliente_codigo': 'codigo_cliente'}
    )

    # pedido_codigo => codigo_pedido
    df_itens = df_itens.rename(
        columns={'pedido_codigo': 'codigo_pedido'}
    )


except Exception as e:
    print(f'Erro ao conectar ou consultar o banco: {e}')


# RELACIONAMENTOS COM MERGE
try:
    # MERGE 1: Junta clientes com pedidos usando a coluna codigo_cliente
    df_merge1 = pd.merge(
        df_clientes,
        df_pedidos,
        on='codigo_cliente'
    )


    # MERGE 2: Junta pedidos com itens do pedido usando a coluna codigo_pedido
    df_merge2 = pd.merge(
        df_merge1,
        df_itens,
        on='codigo_pedido'
    )


    # MERGE FINAL: Junta com a tabela de produtos usando a coluna codigo_produto
    df_final = pd.merge(
        df_merge2,
        df_produtos,
        on='codigo_produto'
    )


    # FILTRO: Mostrar apenas clientes da cidade de São Paulo
    df_sao_paulo = df_final[
       ( 
           (df_final['cidade'] == 'Sao Paulo') |
           (df_final['cidade'] == 'Curitiba')
        
        )
    ]


    # RESULTADO FINAL
    print('\nPedidos de Clientes de São Paulo:\n')

    print(
        df_sao_paulo[
            [
                'nome',
                'sobrenome',
                'cidade',
                'codigo_pedido',
                'data_pedido',
                'produto',
                'valor'
            ]
        ]
    )

except Exception as e:
    print(f'Erro ao processar as informações: {e}')



# Mesmo com SQL
query = """
    -- Liste os pedidos feitos por clientes que moram em São Paulo.
    SELECT 
        tb_clientes.nome, 
        tb_clientes.sobrenome, 
        tb_pedidos.codigo_pedido, 
        tb_pedidos.data_pedido,
        tb_produtos.produto

    FROM tb_pedidos

    JOIN tb_clientes 
        ON tb_pedidos.codigo_cliente = tb_clientes.codigo_cliente

    JOIN tb_itens 
        ON tb_itens.codigo_pedido = tb_pedidos.codigo_pedido

    JOIN tb_produtos 
        ON tb_itens.codigo_produto = tb_produtos.codigo_produto

    WHERE tb_clientes.cidade = 'Sao Paulo' 
       OR tb_clientes.cidade = 'Curitiba';
"""

df_dados = pd.read_sql_query(query, engine)

print('\nDados')
print(df_dados)




# # =========================================================================
# # Merge: Juntar dois dataframes
# df_merge1 = pd.merge(
#     df_clientes,
#     df_pedido,
#     on='codigo_produto'
# )

# # =========================================================================
# Quando os nomes das colunas são diferentes é necessário informar o parâmetro left on e right_on
# df_merge1 = pd.merge(
#     df_clientes,
#     df_pedidos,
#     left_on='codigo_cliente',
#     right_on='cliente_codigo'
# )


