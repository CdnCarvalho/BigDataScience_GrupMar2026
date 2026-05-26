SELECT * FROM tb_usuarios;

SELECT nome, cpf, cidade
FROM tb_usuarios
WHERE cidade = "Sao Paulo";

-- Chave Primária usuário
-- ALTER TABLE 
-- MODIFY COLUMN  INT NOT NULL AUTO_INCREMENT,
-- ADD PRIMARY KEY(codigo_cliente);



/* CHAVES DAS ATIVIDADES */
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
MODIFY COLUMN codigo_item_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item_pedido);


-- ----- CHAVES ESTRANGEIRAS
ALTER TABLE tb_emprestimos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);

ALTER TABLE tb_itens_emprestimos
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);


ALTER TABLE tb_itens_emprestimos
ADD CONSTRAINT fk_emprestimo
FOREIGN KEY (id_emprestimo) REFERENCES tb_emprestimos(id_emprestimo);


/* SELECT COM INNER JOIN */
-- Nomes dos usuários e datas de devolução
SELECT nome, data_devolucao, valor, cpf
FROM tb_emprestimos
INNER JOIN tb_usuarios
	ON tb_usuarios.id_usuario = tb_emprestimos.id_usuario;
    
    
SELECT tb_emprestimos.id_emprestimo, titulo
FROM tb_emprestimos
INNER JOIN tb_itens_emprestimos
	ON tb_itens_emprestimos.id_emprestimo = tb_emprestimos.id_emprestimo
INNER JOIN tb_livros
	ON tb_livros.id_livro = tb_itens_emprestimos.id_livro;


SELECT tb_usuarios.nome, tb_emprestimos.id_emprestimo, tb_livros.id_livro, titulo, data_devolucao
FROM tb_usuarios
JOIN tb_emprestimos
	ON tb_emprestimos.id_usuario = tb_usuarios.id_usuario
JOIN tb_itens_emprestimos
	ON tb_itens_emprestimos.id_emprestimo = tb_emprestimos.id_emprestimo
JOIN tb_livros
	ON tb_livros.id_livro = tb_itens_emprestimos.id_livro;






