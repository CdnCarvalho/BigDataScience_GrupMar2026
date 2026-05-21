
SELECT * FROM cadastro_produtos;

SELECT Produto, Marca FROM cadastro_produtos;
SELECT * FROM cadastro_produtos;
WHERE Marca = 'Logitech';


SELECT * FROM cadastro_produtos
WHERE `Preço Unitario` > 20
--ORDER BY `Preço Unitario` ASC;

SELECT * FROM cadastro_produtos
WHERE Marca = 'Hashtag'
AND `Preço Unitario` <  25;

SELECT * FROM cadastro_produtos
WHERE `tipo do produto` = 'Mouse'
AND (`marca` = 'Logitech' OR `marca` = 'Multilaser');

SELECT Produto, Marca, `Preço Unitario`
FROM cadastro_produtos
WHERE `Preço Unitario` > 20
AND Marca = 'Hashtag'
ORDER BY `Preço Unitario`;

SELECT * FROM cadastro_produtos
WHERE Produto LIKE '%tv%';

SELECT * 
FROM cadastro_produtos
WHERE `Observação` IS NOT NULL
AND `Observação` != '';


/*
SELECT Produto, `Preço Unitario`
FROM cadastro_produtos
ORDER BY `Preço Unitario` DESC;
*/
