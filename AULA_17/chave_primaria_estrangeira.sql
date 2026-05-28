/* CHAVES DAS ATIVIDADES */
-- CHAVE PRIMÁRIA

-- Tabela clientes
ALTER TABLE clientes
MODIFY COLUMN codigo_cliente INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_cliente);

-- Tabela produtos
ALTER TABLE produtos
MODIFY COLUMN codigo_produto INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_produto);

-- Tabela pedidos
ALTER TABLE tb_pedidos
MODIFY COLUMN codigo_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_pedido);

-- Tabela itens
ALTER TABLE tb_itens
MODIFY COLUMN codigo_item INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item);
-- --------------------------------------------------


-- CHAVE ESTRANGEIRA CLIENTE -> PEDIDO
ALTER TABLE tb_pedidos
ADD CONSTRAINT fk_tb_pedidos_clientes
FOREIGN KEY (codigo_cliente)
REFERENCES clientes (codigo_cliente);


-- CHAVE ESTRANGEIRA ITENS -> PEDIDO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_pedidos
FOREIGN KEY (codigo_pedido)
REFERENCES tb_pedidos (codigo_pedido);


-- CHAVE ESTRANGEIRA ITENS -> PRODUTO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_produtos
FOREIGN KEY (codigo_produto)
REFERENCES produtos (codigo_produto);
-- ---------------------------------------------------



-- REMOVER CHAVE ESTRANGEIRA
ALTER TABLE tb_pedidos
DROP FOREIGN KEY fk_tb_pedidos_clientes;

-- REMOVER CHAVE PRIMARIA
ALTER TABLE clientes
ADD PRIMARY KEY (codigo_cliente);
-- Obs: Se houver relacionamento com outras tabelas, é preciso remover a chave estrangeira primeiro.