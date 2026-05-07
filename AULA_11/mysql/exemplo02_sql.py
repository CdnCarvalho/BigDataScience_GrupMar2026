# pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine, text

host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_aula11'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT * FROM tb_produtos"))
    for linha in resultado:
        print(linha)


# INSERIR DADOS COM SQL
# ----------------------------------------------------
# Consulta para inserir dados com SQL
inserir_sql = """
INSERT INTO eletronicos (produto, preco, vendidos) VALUES
('Smartphone Samsung Galaxy A15', 1299.00, 85),
('Notebook Dell Inspiron 15', 3499.00, 28),
('Smart TV LG 50 4K', 2799.00, 41)
"""

# Inserindo dados com SQL
with engine.connect() as conexao:
    conexao.execute(text(inserir_sql))
    conexao.commit()  # Importante para aplicar as mudanças no banco
# ----------------------------------------------------


# USO DO ENGINE.BEGIN()
# ----------------------------------------------------
# begin() para ão precisa do commit no final
with engine.begin() as conexao:
    conexao.execute(text("INSERT INTO ..."))  # commit automático ao final