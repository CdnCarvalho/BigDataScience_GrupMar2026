# Criar um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de Santa Catarina (100 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente. O pescador precisa que você faça um programa que leia o peso de peixes pescados no dia e verifique se há excesso. Se houver peso excedente, mostrar o valor que ele pagará de multa; caso contrário, mostrar uma mensagem dizendo que ele não deve pagar nada (resolver a questão utilizando uma função para calcular a multa caso seja necessário).

# ======================================
# ####### FUNÇÃO - cálculo da multa

def calcular_multa(excesso):
    multa = excesso * MULTA_P_KG
    return multa


# -------------------------------------
# CONSTANTES
# Valores fixos definidos no programa
MULTA_P_KG = 4.00
QUILOS_PERMITIDOS = 100.00


# -------------------------------------
# PROGRAMA PRINCIPAL

try:
    # ENTRADA DE DADOS
    # Pode gerar erro se o usuário digitar algo inválido
    peso_pescado = float(input('Informe o peso dos pescados: '))

except ValueError:
    # Executa se o usuário não digitar um número válido
    print('Erro: informe um valor numérico válido para o peso.')

else:
    # Executa somente se NÃO houver erro na entrada

    if peso_pescado > QUILOS_PERMITIDOS:
        excedente = peso_pescado - QUILOS_PERMITIDOS
        
        # Chamada da função para calcular a multa
        vl_da_multa = calcular_multa(excedente)
        
        print(f'Excesso de Peso! Multa à pagar R$ {vl_da_multa:.2f}')
    
    else:
        print(f'Sem multa à pagar. O peso pescado foi de {peso_pescado}Kg dos {QUILOS_PERMITIDOS}Kg permitidos.')


finally:
    # Sempre executa, independente de erro ou não
    print('Operação finalizada.')