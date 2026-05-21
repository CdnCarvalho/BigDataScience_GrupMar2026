# EXEMPLO 2
from sqlalchemy import create_engine, text

# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'mod2_aula3'


# URL de conexão com o banco, usando SQLAlchemy e PyMySQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Estabelece a conexão
with engine.connect() as conexao:
    # Query: "Linguagem SQL para selecionar todos os registros da tabela produtos"
    query = "SELECT * FROM materiais_construcao"
    # query = "SELECT * FROM materiais_construcao WHERE fornecedor = 'local';"

    # 'text(query)' transforma a string da query em um objeto compatível com SQLAlchemy.
    # 'conexao.execute' executa essa consulta no banco de dados.
    resultados = conexao.execute(text(query))

    for item in resultados:
        print(item)

    # for item in resultados:
    #     print(f"Produto: {item[0]}, Data da Venda: {item[1]}, Categoria: {item[2]}, Loja: {item[3]}, Valor: {item[4]}, Quantidade: {item[5]}")