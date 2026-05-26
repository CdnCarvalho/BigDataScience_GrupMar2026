-- Tabela clientes
ALTER TABLE tb_clientes
MODIFY COLUMN ﻿cod_cliente INT AUTO_INCREMENT,
ADD PRIMARY KEY (﻿codigo_cliente);

-- Tabela produtos
ALTER TABLE tb_produtos
MODIFY COLUMN codigo_produto INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_produto);

-- Tabela pedidos
ALTER TABLE tb_pedidos
MODIFY COLUMN codigo_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_pedido);

-- Tabela itens
ALTER TABLE tb_itens
MODIFY COLUMN codigo_item_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item_pedido);


-- Relacionamento pedidos → clientes
ALTER TABLE tb_pedidos
ADD CONSTRAINT fk_pedidos_cliente
    FOREIGN KEY (cliente_codigo) REFERENCES tb_clientes(cod_cliente)
    ON DELETE CASCADE;
    
ALTER TABLE tb_itens
ADD CONSTRAINT fk_itens_produto
    FOREIGN KEY (item_codigo)
    REFERENCES tb_produtos(codigo_produto)
    ON DELETE CASCADE,
ADD CONSTRAINT fk_itens_pedido
    FOREIGN KEY (pedido_codigo)
    REFERENCES tb_pedidos(codigo_pedido)
    ON DELETE CASCADE;
    

-- Mostre os produtos comprados em cada pedido com suas quantidades.
SELECT tb_pedidos.codigo_pedido, tb_produtos.produto, tb_itens.quantidade
FROM tb_itens
JOIN tb_pedidos ON tb_itens.pedido_codigo = tb_pedidos.codigo_pedido
JOIN tb_produtos ON tb_itens.item_codigo = tb_produtos.codigo_produto;

-- Liste os pedidos feitos por clientes que moram em São Paulo.
SELECT 
tb_clientes.nome, 
tb_clientes.sobrenome, 
tb_pedidos.codigo_pedido, 
tb_pedidos.data_pedido
FROM tb_pedidos
JOIN tb_clientes ON tb_pedidos.cliente_codigo = tb_clientes.cod_cliente
WHERE tb_clientes.cidade = 'São Paulo';
