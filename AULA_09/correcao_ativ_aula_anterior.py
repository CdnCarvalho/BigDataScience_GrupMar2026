# ATIVIDADE 2
# Criar um programa que leia a altura e o peso de N pessoas e 
# mostre seu IMC com a respectiva classificação.
# O cálculo do IMC deverá ser realizado através de uma função.

# Fórmula --> IMC = PESO / (ALTURA * ALTURA)


# -----------------------------------------------------------------
# VERSÃO UTILIZANDO IF e FOR
# FUNÇÃO → apenas calcula e retorna o IMC
def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc  # retorna o valor calculado


# PROGRAMA PRINCIPAL
qtd = int(input('Quantidade de pessoas? '))

for i in range(qtd):
    print(30 * '=')
    print(f'PESSOA {i+1}')
    
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # chamando a função e guardando o resultado
    imc = calcula_imc(peso, altura)

    # agora fazemos a classificação FORA da função
    if imc <= 16.9:
        classificacao = 'Muito abaixo do peso'
    elif imc <= 18.4:
        classificacao = 'Abaixo do peso'
    elif imc <= 24.9:
        classificacao = 'Peso Normal'
    elif imc <= 29.9:
        classificacao = 'Acima do Peso'
    elif imc <= 34.9:
        classificacao = 'Obesidade Grau 1'
    elif imc <= 40:
        classificacao = 'Obesidade Grau 2'
    else:
        classificacao = 'Obesidade Grau 3'

    # exibição dos resultados
    print('\nRESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')
    print('-' * 30)
# ---------------------------------------------------------------------



# VERSÃO UTILIZANDO MATCH CASE E FOR
# FUNÇÃO → apenas calcula e retorna o IMC
def calcula_imc(p, a):
    imc = p / (a ** 2)
    return imc  # retorna apenas o valor


# PROGRAMA PRINCIPAL
qtd = int(input('Quantidade de pessoas? '))

for i in range(qtd):
    print(f'\nPESSOA {i+1}')
    
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # chama a função e recebe o IMC calculado
    imc = calcula_imc(peso, altura)

    
    # CLASSIFICAÇÃO usando match/case
    match imc:
        case imc if imc < 17:
            classificacao = 'Muito abaixo do peso'
        case imc if imc < 18.5:
            classificacao = 'Abaixo do peso'
        case imc if imc < 25:
            classificacao = 'Peso normal'
        case imc if imc < 30:
            classificacao = 'Acima do peso'
        case imc if imc < 35:
            classificacao = 'Obesidade grau 1'
        case imc if imc < 40:
            classificacao = 'Obesidade grau 2'
        case _:
            classificacao = 'Obesidade grau 3'

    
    # EXIBIÇÃO
    print(30 * '=')
    print('RESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')
# ---------------------------------------------------------------------



# ############### VERSÃO UTLIZANDO WHILE ####################
# FUNÇÃO → apenas calcula e retorna o IMC
def calcula_imc(p, a):
    imc = p / (a ** 2)
    return imc


# PROGRAMA PRINCIPAL
continuar = 'S'  # variável de controle do laço

while continuar.upper() == 'S':
    print('\nNOVO CÁLCULO DE IMC')

    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # calcula o IMC
    imc = calcula_imc(peso, altura)

    # CLASSIFICAÇÃO com match/case
    match imc:
        case imc if imc < 17:
            classificacao = 'Muito abaixo do peso'
        case imc if imc < 18.5:
            classificacao = 'Abaixo do peso'
        case imc if imc < 25:
            classificacao = 'Peso normal'
        case imc if imc < 30:
            classificacao = 'Acima do peso'
        case imc if imc < 35:
            classificacao = 'Obesidade grau 1'
        case imc if imc < 40:
            classificacao = 'Obesidade grau 2'
        case _:
            classificacao = 'Obesidade grau 3'


    # EXIBIÇÃO
    print(30 * '=')
    print('RESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')

    # PERGUNTA AO USUÁRIO
    continuar = input('\nDeseja continuar? (S/N): ')

print('\nPrograma encerrado.')
# ---------------------------------------------------------------



# ############### WHILE TRUE ####################
# FUNÇÃO → apenas calcula e retorna o IMC
def calcula_imc(p, a):
    imc = p / (a ** 2)
    return imc



# PROGRAMA PRINCIPAL
while True:
    print('\nNOVO CÁLCULO DE IMC')

    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # calcula o IMC
    imc = calcula_imc(peso, altura)


    # CLASSIFICAÇÃO com match/case
    match imc:
        case imc if imc < 17:
            classificacao = 'Muito abaixo do peso'
        case imc if imc < 18.5:
            classificacao = 'Abaixo do peso'
        case imc if imc < 25:
            classificacao = 'Peso normal'
        case imc if imc < 30:
            classificacao = 'Acima do peso'
        case imc if imc < 35:
            classificacao = 'Obesidade grau 1'
        case imc if imc < 40:
            classificacao = 'Obesidade grau 2'
        case _:
            classificacao = 'Obesidade grau 3'


    # EXIBIÇÃO
    print(30 * '=')
    print('RESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')

  
    # CONTROLE DE SAÍDA
    continuar = input('\nDeseja continuar? (S/N): ').strip().upper()

    if continuar != 'S':
        break  # encerra o laço

print('\nPrograma encerrado.')
# -----------------------------------------------------------------------------