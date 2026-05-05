print(
'''
======================== 
    Caixa Eletrônico 
========================
''')

try:
    saldo = 1000  # saldo atual na conta
    saque = float(input('Quanto deseja sacar? R$ '))  # pode gerar ValueError
    
except ValueError:
    print('Valor inválido! Digite apenas números (ex: 100).')
except KeyboardInterrupt:
    print('\nOperação encerrada pelo usuário')

else:
    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque <= 0:
        print('Valor do saque deve ser maior que zero.')
    else:
        saldo -= saque
        print('\nSaque realizado com sucesso.')
        print(f'Saldo restante: R$ {saldo:.2f}')

finally:
    print('Operação finalizada')

print('\nPrograma encerrado.')