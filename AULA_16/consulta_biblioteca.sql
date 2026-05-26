-- SELECT * FROM TB_EMPRESTIMOS;
-- SELECT * FROM TB_LIVROS;
-- SELECT * FROM TB_USUARIOS;
/*
ALTER TABLE tb_usuarios
MODIFY COLUMN id_usuario INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_usuario);

ALTER TABLE tb_livros
MODIFY COLUMN id_livro INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_livro);
*/
/*
ALTER TABLE tb_alugados
MODIFY COLUMN id_emprestimo INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_emprestimo);
*/
/*
ALTER TABLE tb_itens_emprestados
MODIFY COLUMN id_item INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_item);
*/

/*
ALTER TABLE tb_emprestimos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);
*/
/*
ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);
*/
/*
ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_emprestimo
FOREIGN KEY (id_aluguel) REFERENCES tb_aluguel(id_aluguel);
*/


/*
-- MOSTRAR OS IDs DE LIVROS QUE NÃO ESTÃO NA TB_LIVROS, MAS ESTÃO NO EMPRÉSTIMOS (SE ACONTECER ISSO, GERA UM ERRO)
SELECT * FROM tb_itens_emprestados 
WHERE id_livro NOT IN (SELECT id_livro FROM tb_livros);
*/


/*MÃO NA MASSA*/

-- Consultas com WHERE
-- Mostre os livros emprestados
SELECT tb_livros.titulo
FROM tb_livros, tb_itens_alugados
WHERE tb_livros.id_livro = tb_itens_alugados.id_livro;
-- CONTINUA NA DE BAIXO

SELECT  tb_livros.id_livro, tb_livros.titulo
FROM tb_livros, tb_itens_alugados, tb_alugados
WHERE tb_livros.id_livro = tb_itens_alugados.id_livro
  AND tb_alugados.id_aluguel = tb_itens_alugados.id_aluguel
  AND tb_alugados.data_aluguel = '2024-10-10';



/* **** EXEMPLOS DE JOIN ****/
-- Mostrar o nome dos usuários e as datas dos alugueis e devolução
SELECT 
  tb_usuarios.nome,
  tb_alugados.data_aluguel,
  tb_alugados.data_devolucao
FROM 
  tb_usuarios
JOIN 
  tb_alugados ON tb_usuarios.id_usuario = tb_alugados.id_usuario;
  
  
-- Mostrar os nomes dos livros que foram emprestados e os códigos dos empréstimos
SELECT 
  tb_livros.titulo,
  tb_itens_alugados.id_aluguel
FROM 
  tb_livros
JOIN 
  tb_itens_alugados ON tb_livros.id_livro = tb_itens_alugados.id_livro;
  -- Dar continuidade na q está logo abaixo....



-- Mostrar os nomes dos livros e id dos livros que foram emprestados e os códigos dos empréstimos
-- Mostrar as datas de devolução, aluguel e valor
-- Mostrar o nome e o id do usuário que alugou
-- No mês de novembro
SELECT 
  tb_usuarios.id_usuario,
  tb_usuarios.nome,
  tb_alugados.data_aluguel,
  tb_alugados.data_devolucao,
  tb_alugados.valor,
  tb_livros.id_livro,
  tb_livros.titulo,
  tb_itens_alugados.id_aluguel
FROM 
  tb_livros
JOIN tb_itens_alugados 
	ON tb_livros.id_livro = tb_itens_alugados.id_livro
JOIN tb_alugados 
	ON tb_itens_alugados.id_aluguel = tb_alugados.id_aluguel
JOIN tb_usuarios 
	ON tb_usuarios.id_usuario = tb_alugados.id_usuario
WHERE tb_alugados.data_devolucao BETWEEN '2024-11-01' AND '2024-11-30';


/*
-- APELIDOS NO JOIN
SELECT 
  ie.id_emprestimo,
  SUM(l.valor_emprestimo) AS total_emprestimo
FROM 
  tb_itens_emprestados ie
JOIN 
  tb_livros l ON ie.id_livro = l.id_livro
GROUP BY 
  ie.id_emprestimo
ORDER BY 
  ie.id_emprestimo;
*/