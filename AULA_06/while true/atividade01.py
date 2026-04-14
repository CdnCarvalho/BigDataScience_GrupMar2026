# Crie um algoritmo que receba o salário de um funcionário e calcule um aumento de 15% 
# Mostre no final o antigo salário, o valor do aumento e o novo salário.
# Não sabemos quantos funcionários serão informados.

while True:
    salario = float(input('Digite o salário do funcionário: ')) 
    aumento = salario * 0.15
    novo_salario = salario + aumento

    print(f'O antigo salário era de R${salario:.2f}')  
    print(f'O valor do aumento é de R${aumento:.2f}')   
    print(f'O novo salário é de R${novo_salario:.2f}')

    resposta = input('\nDeseja continuar? [S/N] ').upper()
    if resposta == 'N':
        break

print('Fim do programa')


# Crie um algoritmo que receba o salário de um funcionário e calcule um aumento de 15% para 
# funcionários de TI e 10% para os demais funcionários.
# Mostre no final o antigo salário, o valor do aumento e o novo salário.
# Não sabemos quantos funcionários serão informados.
# O programa deve perguntar se o funcionário é de TI ou não.
while True:
    salario = float(input('Digite o salário do funcionário: '))
    setor = input('Qual o setor do funcionário? [TI/OUTROS]: ').upper().strip()

    if setor == 'TI':
        aumento = salario * 0.15
        print('\nFuncionário de TI 15%')
        # print(f'Salário antigo R${salario:.2f}')
        # print(f'Valor do aumento é de R${aumento:.2f}')
        # print(f'O novo salário é de R${novo_salario:.2f}')
    else: 
        aumento = salario * 0.10
        print('\nFuncionário de outros setores 10%')
        # print(f'Salário antigo R${salario:.2f}')
        # print(f'Valor do aumento é de R${aumento:.2f}')
        # print(f'O novo salário é de R${novo_salario:.2f}')

    novo_salario = salario + aumento
    print(f'Salário antigo R$ {salario:.2f}')
    print(f'Valor do aumento é de R$ {aumento:.2f}')
    print(f'O novo salário é de R$ {novo_salario:.2f}')

    resposta = input('\nDeseja continuar? [S/N] ').upper()
    if resposta == 'N':
        break

print('Fim do programa')


# Atividade 03
# Meta mensal
meta = 15000

while True:
    # Entrada de dados
    vendas = float(input("Digite o valor total de vendas do mês: "))
    
    # Cálculo do percentual de atingimento
    percentual = (vendas / meta) * 100
    
    # Exibição dos resultados
    print(f"Vendas: R${vendas:.2f}")
    print(f"Atingimento da meta: {percentual:.2f}%")
    
    # Pergunta se deseja continuar
    continuar = input("Deseja informar outro vendedor? (s/n): ").lower()
    
    if continuar == "n":
        break