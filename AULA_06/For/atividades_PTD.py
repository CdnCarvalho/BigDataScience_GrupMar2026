# ATIVIDADE 1 - Notas de 10 alunos (Versão 2 FOR)

# Algoritmo Recebe 4 notas e calcula a média para cada um dos 10 alunos
# As nostas são informadas pelo usuários.
for aluno in range(10):  # repete o bloco para 10 alunos
    print(f"\n---- Aluno {aluno + 1} ----")  # mostra o número do aluno (1 a 10)
    soma_notas = 0  # inicializa a soma das notas para o aluno atual

    for nota in range(4):  # repete o bloco para 4 notas
        valor_nota = float(input(f"Digite a nota {nota + 1}: "))  # recebe a nota do usuário
        soma_notas += valor_nota  # acumula a soma das notas

    media_final = soma_notas / 4  # calcula a média final
    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais
    # =============================================================

# ATIVIDADE 1 VERSÃO 2 - Usando 4 variáveis e apenas 1 FOR
for aluno in range(3):  # repete o bloco para 10 alunos
    print(f"\n---- Aluno {aluno + 1} ----")  # mostra o número do aluno (1 a 10)
    soma_notas = 0  # inicializa a soma das notas para o aluno atual

    n1 = float(input(f"Digite a nota Nota 1: ")) # recebe a nota do usuário
    n2 = float(input(f"Digite a nota Nota 2: "))
    n3 = float(input(f"Digite a nota Nota 3: "))
    n4 = float(input(f"Digite a nota Nota 4: "))
    
    media_final = (n1 + n2 + n3 + n4) / 4  # acumula a soma das notas

    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais

# -------------------------------------------------------------------------------------------------------------


# ATIVIDADE 2
# Algoritmo que recebe 10 valores de vendas e calucula o desconto de 10% para vendas acima de R$ 1000,00.

for venda in range(3):  # repete o bloco para 10 vendas
    print(f"\n---- Venda {venda + 1} ----")  # mostra o número da venda (1 a 10)
    valor_venda = float(input(f"Digite o valor da venda: "))  # recebe o valor da venda do usuário
    desconto = 0  # inicializa o desconto
    novo_valor = valor_venda  # inicializa o novo valor como o valor original da venda
    
    if valor_venda > 1000:
        desconto = valor_venda * 0.10  # calcula o desconto de 10%
        novo_valor = valor_venda - desconto  # calcula o valor a ser pago após o desconto
    

    print(f"O valor da venda é: R$ {valor_venda:.2f}")  # exibe o valor normal da venda
    print(f"O valor do desconto é: R$ {desconto:.2f}")  # exibe o valor do desconto
    print(f"O valor a ser pago é: R$ {novo_valor:.2f}")  # exibe o valor a ser pago
