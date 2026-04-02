# ###### ATIVIDADES INICIAIS ######

# REPOSITÓRIO GITHUB - AULA 02
# ENUNCIADO:
# 1 - Crie um programa, que receba um número e mostre na saída o seu dobro, o triplo e o seu quadrado:
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
quadrado = num ** 2
print(f"O número é {num}")
print("O dobro do número é: ", dobro)
print("O triplo do número é: ", triplo)
print("O quadrado do número é: ", quadrado)

# -------------------------------------------------------------------------------


# REPOSITÓRIO GITHUB - AULA 01
# ENUNCIADO:
# 2 - Faça um programa que leia um número em metros e converta-o para centímetros e milímetros.
n = float(input("Digite um número em metros: "))
centimetro = n * 100
milimetro = n * 1000
# milimetro2 = centimetro * 10
print(f"{n} metros é igual a {centimetro} centímetros e {milimetro} milímetros")

# -------------------------------------------------------------------------------

# ######## PTD
# REPOSITÓRIO GITHUB - AULA 02 
# ENUNCIADO:
# 2.	Construir um algoritmo, no qual o usuário digitará 2 números e o programa exibirá o resultado das quatro operações básicas da matemática no final (soma, subtração, divisão, multiplicação). 
# OBS: O programa deve exibir o resultado de cada operação em uma linha diferente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"A soma é: {soma}")
print(f"A subtração é: {subtracao}")
print(f"A multiplicação é: {multiplicacao}")
print(f"A divisão é: {divisao}")

# -------------------------------------------------------------------------------


# ENUNCIADO:
# Implemente um algoritmo que leia, ou seja, receba 4 notas de um aluno, retire a média e mostre o resultado na tela.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é: {media}")