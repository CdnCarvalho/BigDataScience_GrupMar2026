# IMPORTAÇÃO DAS FUNÇÕES
# Aqui estamos trazendo as funções do arquivo operacoes.py
# Informamos: Da pasta auxiliar, do arquivo operacoes, importe as
# funções dobro, triplo, quadrado e metade.
from auxiliar.operacoes import dobro, triplo, quadrado, metade

# ##### EXEMPLO 03 MODULARIZAÇÃO #####
# def dobro(n):
#     return n * 2

# def triplo(n): 
#     return n * 3

# def quadrado(n):
#     return n ** 2

# def metade(n):
#     return n / 2


# Algoritmo que usuário informa dois números e escolhe se quer o dobro, ou triplo, ou o quadrado 
# calcular a metade
n = int(input('Informe o número: '))
print('\n///// MENU DE OPÇÕES /////\n[1] - Dobro\n[2] - Triplo\n[3] - Quadrado - \n[4] - Metade')
opcao = int(input('\nDigite a opção desejada: '))

match opcao:
    case 1:
        reposta = dobro(n)
    case 2:
        reposta = triplo(n)
    case 3:
        reposta = quadrado(n)
    case 4:
        reposta = metade(n)  # pedir depois
    case _:
        reposta = 'Opção inválida'

print(f'Resultado: {reposta}')
# pedir para dar mais uma opção: calcular a metade