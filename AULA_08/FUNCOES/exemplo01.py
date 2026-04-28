# Funções em Python
# são bloco de código que podem ser reutilizados
# as funções são definidas com a palavra reservada "def",
# Geralmente as funções tem um nome descritivo 
# e são criadas no início do código.
# As funções podem ou não receber parâmetros e retornar valores.

# ###### EXEMPLO 01
# Definindo uma função
def saudacao():
    print("Olá! Bem-vindo à análise de dados.")

saudacao()
saudacao()  # repare: mesma rotina, chamada de novo

# for i in range(5):
#     saudacao()
# ---------------------------------------------------------------



# ###### EXEMPLO 02
def saudacao_aluno(nome):
    print(f"Olá, {nome}! Pronto para analisar dados?")

saudacao_aluno("Ana")
saudacao_aluno("Carlos")
# ---------------------------------------------------------------



# ###### EXEMPLO 03.1
def soma(a, b=0):  # parâmetro com valor default
    resultado = a + b
    # print(f"A soma é {resultado}")  # não printar
    return resultado


num1 = 5
num2 = 3
resposta = soma(num1, num2)
print(f"A resposta retornada é {resposta}")
# ---------------------------------------------------------------



# ###### EXEMPLO 03.2
for i in range(3):
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    resposta = soma(num1, num2)
    print(f"A resposta retornada é {resposta}")
# ---------------------------------------------------------------


