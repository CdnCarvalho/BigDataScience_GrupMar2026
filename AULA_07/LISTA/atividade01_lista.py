# Segunda parte
# Crie um algoritmo que receba 10 números e guarde os 
# valores pares e ímpares de forma separada e mostre-os ao final

pares = []
impares = []
for i in range(10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        # print(f'O número {i} é impar')

print(f'Números pares {pares}')
print(f'Números ímpares {impares}')


# --------------------------------------------------------
# Versão com While True
pares = []
impares = []

contador = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
    contador += 1
    
    if contador == 10:
        break

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")