# =========================================
# ROTEIRO DIDÁTICO - VARIÁVEIS + OPERAÇÕES
# =========================================

# =========================================================
# BLOCO 1 
# =========================================================

# Exemplo 1
nome = 'João'
idade = 20
# ano_nascimento = 2026 - idade

# nome = "pedro"
# idade = 21

print(f'Nome: {nome}')
print("Idade:", idade)
# print("Ano de nascimento:", ano_nascimento)

valor_produto = 50
quantidade = 2

print(valor_produto)
print(quantidade)

# ----------------------------------------------------------

# Atividade:
# nome
# idade
# bairro


# Fala sugerida:
# "Guardamos valores para usar depois no programa."

# =========================================================
# BLOCO 2 - OPERADORES MATEMÁTICOS
# =========================================================

a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
mod = a % b
parte_inteira = a // b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(mod)
print(parte_inteira)


# =========================================================
# BLOCO 3 - ATRIBUINDO RESULTADOS EM VARIÁVEIS
# =========================================================
preco = 30
quantidade = 3

total = preco * quantidade

print(total)
# "Guardamos o resultado para poder reutilizar depois."

# -------------------------------------------------------------------
# ATIVIDADE:
# Outro exemplo
salario = 2000
bonus = 500

salario_total = salario + bonus

print(salario_total)


# =========================================================
# BLOCO 4 - USANDO RESULTADOS EM NOVOS CÁLCULOS
# =========================================================

# ORIENTAÇÃO:
# Mostrar encadeamento de variáveis (isso prepara para média e outros cálculos)

valor1 = 40
valor2 = 20
qtd_pessoas = 2

total = valor1 + valor2
total_pessoa = total / qtd_pessoas

print(total)
print(total_pessoa)

# "Podemos usar o resultado de uma conta em outra."

# Outro exemplo
distancia1 = 100
distancia2 = 50

distancia_total = distancia1 + distancia2
consumo_por_litro = 10  # o carro faz 10 km com 1 litro
combustivel = distancia_total / consumo_por_litro

print(distancia_total)
print(combustivel)


# =========================================================
# BLOCO 5 - INTRODUÇÃO AO INPUT (SEM FOCO EM PROBLEMA FINAL)
# =========================================================

# ORIENTAÇÃO:
# Aqui o aluno passa a fornecer os valores
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
ano_atual = 2026
ano_nascimento = ano_atual - idade  # Erro

# -----------------------------------------------------------------

numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))

resultado = numero1 + numero2
print(resultado)



# -----------------------------------------------------------------
# Exemplo com cálculo
n1 = 10
n2 = 5

resultado = n1 + n2

print(f"O resultado da soma entre {n1} e {n2} é {resultado}")

