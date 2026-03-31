# ### VARIÁVEIS ###
# Variáveis são espaços reservados na memória do computador para armazenar dados.

# ### ATRIBUIÇÃO ###
# A atribuição é o processo de atribuir um valor a uma variável.
# Sintaxe: nome_da_variável = valor

# ### EXEMPLOS DE ATRIBUIÇÃO: ###
# nome = "João"
# idade = 25
# preco = 10.99

# No contexto acima, lê-se: 
# "nome recebe a string 'João'", "idade recebe o inteiro 25" e "preço recebe o float 10.99".

# ### TIPOS BÁSICOS DE VARIÁVEIS: ###
# String: São sequências de caracteres, como "João", "Python" ou "123".
# Inteiro: São números inteiros, como 1, 2, 3, 4, 5, etc.
# Float: São números decimais, como 1.5, 2.7, 3.14, etc.
# Booleano: São valores lógicos, como True (verdadeiro) ou False (falso).

# PYTHON E A TIPAGEM DINÂMICA:
# O Python é uma linguagem de programação de tipagem dinâmica, o que significa,
# que o tipo de uma variável é determinado pelo valor que ela recebe, e não,
# pelo tipo declarado.
# Por exemplo, se eu atribuir um valor inteiro a uma variável, o Python,
# entenderá que essa variável é do tipo inteiro. Se eu atribuir um valor,
# decimal a essa mesma variável, o Python entenderá que essa variável é do,
# tipo float.


# ### EXEMPLOS DE OPERAÇÕES ARITMÉTICA: ###
# Soma: +
# Subtração: -
# Multiplicação: *
# Divisão: /
# Módulo (resto da divisão): %
# Exponenciação: **

# n1 = 5
# n2 = 2
# soma = n1 + n2
# subtracao = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2
# modulo = n1 % n2
# exponenciacao = n1 ** n2

# ### PRÁTICAS NO VSCODE ###
# Comentar linhas: Ctrl + ;
# Interromper o código executado no terminal: Ctrl + C
# Limpar o terminal: Clicar nos três pontos no canto superior direito do terminal e selecionar "Clear Terminal"


# EXEMPLO 1 - Perguntar e mostrar uma informação simples
# Enunciado: Peça ao usuário para digitar o nome e depois cumprimente-o.
nome = input("Qual é o seu nome? ")
print("Olá,", nome, "! Seja bem-vindo(a) ao curso de Python!")


# ATIVIDADE 1 - Usando duas variáveis e exibindo na mesma frase
# Enunciado: Peça o nome da cidade e o estado onde o usuário mora, depois exiba ambos.
cidade = input("Em qual cidade você mora? ")
estado = input("E em qual estado fica essa cidade? ")
print("Você mora na cidade de", cidade, "que fica no estado de", estado + ".")
# -----------------------------------------------------------


# -----------------------------------------------------------
# EXEMPLO 2 - Criando variáveis numéricas
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resposta = n1 * n2
print(f'O resultado é {resposta}')

# ATIVIDADE 2 - Criando variáveis numéricas e exibindo resultados
# Enunciado: Peça a idade do usuário e calcule o ano de nascimento.
idade = int(input("Quantos anos você tem? "))
ano_atual = 2025
ano_nascimento = ano_atual - idade
print("Você nasceu em", ano_nascimento, ".")


# ATIVIDADE 3
# Enunciado: Descubra quantos ingressos de cinema podem ser comprados com o valor disponível.
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
valor_disponivel = float(input("Digite quanto dinheiro você tem para a compra: "))
quantidade = int(valor_disponivel // preco_unitario)
print("Com R$", valor_disponivel, "você pode comprar", quantidade, "ingresso(s).")
# ------------------------------------------------------------

# EXEMPLO 3 - Algoritmos com mais de uma operação
# Enunciado: Calcule o valor total de uma compra com desconto de 10%.
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco * quantidade
desconto = total * 0.1
valor_final = total - desconto
print("O valor total da compra com desconto é:", valor_final)

# ATIVIDADE 4 - Aumento de salário
# Enunciado: Calcule o novo salário de um funcionário com aumento de 15%.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)
