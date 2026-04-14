# While 

# Exemplo 01
# contagem até 10
i = 1
while i <= 10:
    print(f'{i}', end=' ')
    i += 1  # se esquecer o i += 1, entra em loop infinito


# Exemplo 02
# Soma dois números
i = 1
while i <= 3:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    soma = num1 + num2
    i += 1

print(f'A soma dos números é: {soma}')


# Exemplo 03
# Soma números até que o usuário digite 0
n = 1
soma = 0
while n != 0:
    n = int(input("Digite um número: "))
    soma += n

print(f'A soma dos números é: {soma}')


# Exemplo 04
# O algoritmo deve solicitar ao usuário um número e pergunatar se ele quer continuar.
# Se o usuário digirar N, o algoritmo deve parar. 
resposta = 'S'
soma = 0
while resposta != 'N':
    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        soma += numero

    resposta = input("Deseja continuar? [S/N]: ")

print(f'A soma dos números pares é: {soma}')