# ======================================
# ####### VERSÃO 1 - COM LISTA E FOR

# FUNÇÃO → calcula total e média
def calcular_vendas(lista_vendas):
    total = sum(lista_vendas)              # soma das vendas
    media = total / len(lista_vendas)      # calcula a média
    return total, media


# -----------------------------------
# PROGRAMA PRINCIPAL

contador = 1  # controle de vendedor

while True:
    print('\n' + 30 * '=')
    print(f'VENDEDOR {contador}')

    vendas = []  # lista para armazenar as 4 vendas

    try:
        # coleta das 4 vendas usando for
        for i in range(4):
            valor = float(input(f'Informe a venda {i+1}: '))
            vendas.append(valor)

    except ValueError:
        # erro caso o usuário digite algo inválido
        print('Erro: informe apenas valores numéricos para as vendas.')

    else:
        # executa se não houver erro

        total, media = calcular_vendas(vendas)

        print('\nRESULTADO:')
        print(f'Total de vendas: R$ {total:.2f}')
        print(f'Média de vendas: R$ {media:.2f}')

    finally:
        # sempre executa
        print('Processo finalizado para este vendedor.')

    # controle do loop
    opcao = input('\nDeseja cadastrar outro vendedor? (S/N): ').strip().upper()

    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')