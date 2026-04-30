import random
import os

# função para somar
def somar(a, b):
  soma = a + b
  return soma


# função para subtrair
def subtrair(a, b):
  subtracao = a - b
  return subtracao


# função para multiplicar
def multiplicar(a, b):
  multiplicacao = a * b
  return multiplicacao


# função para dividir
def dividir(a, b):
  divisao = a / b
  return divisao


# Início
os.system('cls')
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print(f'Os números sorteados foram {n1} e {n2}')

print('\nEscolha uma operação: ')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')


# match case
opcao = int(input('\nDigite a opção desejada: '))
match opcao:
  case 1:
    print('Você escolheu somar')
    print(somar(n1, n2))
  case 2:
    print('Você escolheu subtrair')
    print(subtrair(n1, n2))
  case 3:
    print('Você escolheu multiplicar')
    print(multiplicar(n1, n2))
  case 4:
    print('Você escolheu dividir')
    print(dividir(n1, n2))
  case _:
    print('Opção inválida')