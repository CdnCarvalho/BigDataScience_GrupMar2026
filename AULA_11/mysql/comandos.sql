Conectar-se ao MySQL e Habilitar o Local_Infile no Cliente:
mysql --local_infile -u root -p

-- Criando um Banco de Dados
CREATE DATABASE bd_aula11;

-- Definindo o banco a ser usado
USE bd_aula11;

-- Criar uma Tabela 
CREATE TABLE tb_produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(255),
    preco DECIMAL(10, 2),
    vendidos INT
    );

-- Inserir dados na Tabela
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Mouse Logitech MX Master 3', 699.00, 82)


-- Verificar o local do diretório permitido
SHOW VARIABLES LIKE 'secure_file_priv'; 

-- Verificar a permissão para permitir arquivos no MySQL
SHOW VARIABLES LIKE 'local_infile';

-- Habilitar a permissão para arquivos usando global
SET GLOBAL local_infile=1;

-- Inserindo o conteúdo do arquivo.csv na tabela
-- LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\base1.csv'
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.7\\Uploads\\base1.csv'
INTO TABLE tb_produtos 
FIELDS TERMINATED BY ';' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(produto, preco, vendidos);

-- Mostrando o conteúdo da tabela
SELECT * FROM tb_produtos;

-- INSERT para 1 produto
inserir_sql_um = """
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Fone de Ouvido JBL Tune 510BT', 299.00, 120)
"""

-- Para inserir
inserir_sql = """
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Smartphone Samsung Galaxy A15', 1299.00, 85),
('Notebook Dell Inspiron 15', 3499.00, 28),
('Smart TV LG 50 4K', 2799.00, 41)
"""