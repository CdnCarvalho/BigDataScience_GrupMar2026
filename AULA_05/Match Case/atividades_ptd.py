# ATIVIDADE 1
# Informe o código da região
codigo = int(input("Informe o código da região: "))
# Verifica a região correspondente ao código
match codigo:
    case 1:
        print('Sul')
    case 2:
        print('Norte')
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case num if num == 5 or num == 6:
        print('Nordeste')
    case 7 | 8 | 9:
        print('Sudeste')
    case 10:
        print('Centro-Oeste')
    case _:
        print('Prouduto Importado')

# ----------------------------------------------------------------

# ATIVIDADE 2
# Notas dos alunos
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
optativa = float(input("Digite Optativa: "))

# Vereifica se o aluno realizou a optativa e se a nota é maior
# que a nota 1 ou maior que a nota 2
if optativa != -1 and optativa > n1 or optativa > n2:
    if n2 < n1:
        n2 = optativa
    else:
        n1 = optativa

media = (n1 + n2) / 2

match media:
    case m if m > 6:
        print(f"Aluno Aprovado com média {media}")
    case m if 3 <= m <= 6:
        print(f"Aluno em Recuperação com média {media}")
    case _:
        print(f"Aluno Reprovado com média {media}")
# ----------------------------------------------------------------


# ATIVIDADE 3
vl_compra = float(input("Informe o valor da compra: "))
# forma_pagamento = int(input("Informe a forma de pagamento (1 - À vista, 2 - Parcelado): "))
forma_pagamento = input("Informe a forma de pagamento (À vista, Débito, Crédito, Pix, Cheque): ").upper().strip()

sucesso = True

match forma_pagamento:
    case "À VISTA":
        vl_final = vl_compra - (vl_compra * 10 / 100)
    case "PIX":
        vl_final = vl_compra
    case "DÉBITO":
        vl_final = vl_compra + (vl_compra * 5 / 100)
    case "CRÉDITO":
        vl_final = vl_compra + (vl_compra * 8 / 100)
    case "CHEQUE":
        vl_final = vl_compra + (vl_compra * 12 / 100)
    case _:
        print(f"Forma de pagamento Inválida: {forma_pagamento}")
        sucesso = False

if sucesso:
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor da compra: {vl_compra:.2f}")
    print(f"Total a pagar: {vl_final:.2f}") 
else:
    print("Por favor, escolha uma opção válida.")

