# Criar um programa que ajude um pescador a controlar sua produtividade. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de Santa Catarina (100 quilos),
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# O pescador precisa que você faça um programa, que leia o peso dos peixes pescados
# no dia e verifique se há excesso. 
# Se houver peso excedente, mostrar o valor que ele pagará de multa; 
# Caso contrário, mostrar uma mensagem dizendo que ele não deve pagar nada 
# (resolver a questão utilizando uma função para calcular a multa caso seja necessário).

def calcular_multa(excesso):
    multa = excesso * MULTA_P_KG
    return multa


MULTA_P_KG = 4.00
QUILOS_PERMITIDOS = 100.00
peso_pescado = float(input('Informe o peso dos pescados: '))

if peso_pescado > QUILOS_PERMITIDOS:
    excedente = peso_pescado - QUILOS_PERMITIDOS
    vl_da_multa = calcular_multa(excedente)
    print(f'Excesso de Peso! Multa à Pagar R$ {vl_da_multa}')
else:
    print(f'Sem multa à pagar. O peso pescado foi de {peso_pescado}Kg dos {QUILOS_PERMITIDOS}Kg permitidos.')