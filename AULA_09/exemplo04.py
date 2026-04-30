import random

def gerar_numeros(qtd, ini, fim):
  lst_num = [random.randint(ini, fim) for i in range(qtd)]

  return lst_num



# função para somar
def somar(n1, n2):
  soma = n1 + n2
  return soma


# função para subtrair
def subtrair(n1, n2):
  subtracao = n1 - n2
  return subtracao


# função para multiplicar
def multiplicar(n1, n2):
  multiplicacao = n1 * n2
  return multiplicacao


# função para dividir
def dividir(n1, n2):
  divisao = n1 / n2
  return divisao



# ######  Início do programa principal
# n1 = random.randint(1, 10)
# n2 = random.randint(1, 10)

lista = gerar_numeros(2, 1, 10)
print(lista)
print(f'\nPrimeiro: {lista[0]}')
print(f'Segundo: {lista[1]}')


print('\nEscolha um numero para a operação: ')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')


# match case
opcao = int(input('Digite a opção desejada: '))
match opcao:
  case 1:
    print('Você escolheu somar')
    print(somar(lista[0], lista[1]))
  case 2:
    print('Você escolheu subtrair')
    print(subtrair(lista[0], lista[1]))
  case 3:
    print('Você escolheu multiplicar')
    print(multiplicar(lista[0], lista[1]))
  case 4:
    print('Você escolheu dividir')
    print(dividir(lista[0], lista[1]))
  case _:
    print('Opção inválida')