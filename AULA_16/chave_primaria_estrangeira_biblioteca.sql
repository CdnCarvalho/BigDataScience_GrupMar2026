-- CHAVE PRIMÁRIA
ALTER TABLE tb_usuarios
MODIFY COLUMN id_usuario INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_usuario);

ALTER TABLE tb_livros
MODIFY COLUMN id_livro INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_livro);

ALTER TABLE tb_emprestimos
MODIFY COLUMN id_emprestimo INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_emprestimo);

ALTER TABLE tb_itens_emprestados
MODIFY COLUMN id_item INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_item);


-- CHAVE ESTRANGEIRA
ALTER TABLE tb_emprestimos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);

ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);

ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_emprestimo
FOREIGN KEY (id_emprestimo) REFERENCES tb_emprestimos(id_emprestimo);