# Exceções

# ------------------------------------------------------------- NameError: Variável não definida
print(nome)



# ------------------------------------------------------------- ValueError: Digitar letras ao invés de números
idade = int(input('Informe a idade: '))
print(idade)



# ------------------------------------------------------------ TypeError: Operação entre tipos incompatíveis (Strings com ints ou floats)
n1 = int(input('Informe o número: '))
n2 = input('Informe o número: ')

total = n1 + n2
print(f'Total: {total}')



# ----------------------------------------------------------- ZeroDivisionError: Divisão por zero
num1 = float(input('Inorme um número: '))
num2 = float(input('Informe outro número: '))

resultado = n1 / n2
print(f'Resultado:  {resultado}')



# ----------------------------------------------------------- IndexError: Índice fora do intervalo da lista
lst_nomes = ['maria', 'joão', 'pedro', 'tiago']
posicao = int(input('Informe a classificação: '))
print(lst_nomes[5])
