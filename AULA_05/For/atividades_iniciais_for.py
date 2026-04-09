# Gabarito – Introdução ao for
# Conjunto de exercícios iniciais para praticar a estrutura de repetição for em Python.


# ------------------------------------------------------------------
# Exercício 1 – Mensagem repetida
# Enunciado: Exiba a mensagem "Estudando Python!" 5 vezes.

for _ in range(5):
    print("Estudando Python!")

# Usamos _ quando não precisamos do número da repetição.


# ------------------------------------------------------------------
# Exercício 2 – Soma de valores
# Enunciado: Soma 5 vendas informadas pelo usuário.
soma = 0
for i in range(5):
    venda = float(input(f"Digite a venda {i + 1}: "))
    soma = soma + venda

print(f"O total das vendas é de: R$ {soma:.2f}")
# A soma é exibida ao final da execução.


# ------------------------------------------------------------------
# Exercício 2 – Soma apenas os valores acima 1000
# Enunciado: Recebe 5 vendas, informadas pelo usuário 
# e soma apenas os valores acima de R$ 1000,00.
soma = 0
for i in range(5):
    venda = float(input(f"Digite a venda {i + 1}: "))

    if venda > 1000:
        soma = soma + venda

print(f"O total das vendas é de: R$ {soma:.2f}")
# A soma é exibida ao final da execução.