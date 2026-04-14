# COMANDO FOR 
# O comando for é uma estrutura de repetição em Python.
# Ele é usado para executar um bloco de código várias vezes, de forma controlada.
# Normalmente, usamos o for junto com a função range(), que gera uma sequência de números.

# ************** EXPLICANDO A ESTRUTURA FOR ABAIXO: ***********************
# for i in range(3):

####  for: palavra-chave que inicia a repetição
####  i: variável de controle que assume valores a cada repetição
####  in: conecta o for com a sequência a ser repetida
####  range(3): função que gera a sequência (neste caso: 0, 1, 2)
####  : (dois-pontos): obrigatório ao final da linha que inicia o for
####  OBS: O bloco que será repetido vem logo abaixo, com INDENTAÇÃO!


# ************** INDENTAÇÃO (Recuo Obrigatório no Python) *****************
# Python **não usa chaves {}, nem begin/end como em outras linguagens p/
# informar o que está dentro ou fora da estrutura For.
# O que define o bloco de código a ser repetido é o recuo (IDENTAÇÃO).

# EXEMPLO:
# for i in range(3):
#     print(i)  # <- esta linha está dentro do for, pois está indentada
# print("fim")  # <- esta linha está fora do for


# ---------------------------------------------------------------------------------------
# EXEMPLOS PRÁTICOS - ESTRUTURA DE REPETIÇÃO FOR
# ----------------------------------------------------------------------------------------
# Exemplo 1 – Repetição simples com mensagem
for n in range(5):  # repete o bloco abaixo 5 vezes (valores de 0 até 4)
    print("olá mundo")  # exibe a mensagem "olá mundo" a cada repetição

# ----------------------------------------------------------------------------------------
# Exemplo 2 – Contando de 0 até 10
for n in range(11):  # n vai assumir os valores 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10
    print(n)  # mostra o valor atual de n



# ----------------------------------------------------------------------------------------
# Exemplo 6 – Soma 3 pares de números (Usuário informa dois números a cada iteração)
for n in range(3):  # repete o bloco 3 vezes 
    print(f'\n---- Rodada {n + 1}')  # Nº da iteração (1, 2 ou 3)
    n1 = float(input("Informe o primeiro número: "))  # recebe o nome da pessoa
    n2 = float(input("Informe o segundo número: "))  # recebe o nome da pessoa
    soma = n1 + n2
    print(f'Resultado: {soma}')  


# ----------------------------------------------------------------------------------------
# Exemplo 7 – Somando valores informados pelo usuário
soma = 0.  # inicializa a variável soma com valor 0.0

for num in range(3):  # repete 3 vezes
    numero = float(input("Digite um número: "))  # recebe um número real (float) do usuário
    soma += numero  # adiciona o número digitado à variável soma (acumulador)

print(f'O total é de {soma}')  # mostra o valor total somado


# Exemplo 8 - Recebe 5 vendas e soma apenas as vends maiores que 100
soma = 0.  # inicializa a variável soma com valor 0.0
for i in range(3):
    venda = float(input("\nInforme a venda: "))
    if venda >= 100:
        soma = soma + venda
        print(f"Valor R$ {venda} somado.")
    else:
        print(f"Valor R$ {venda} não somado.")
    
print(f'\nTOTAL DE: R$ {soma}')  # mostra o valor total somado
