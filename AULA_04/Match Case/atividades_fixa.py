###### ATIVIDADE 1
# Número positivo ou negativo
num = float(input("Digite um número: "))
# Verifica se o número é positivo, negativo ou zero
match num:
    case num if num > 0:
        print(f"{num} é positivo")
    case num if num < 0:
        print(f"{num} é negativo")
    case 0:
        print(f"{num} Zero é positivo")

# --------------------------------------------------------


###### Atividade 2
valor = float(input("Digite um valor de venda: "))

match valor:
    case v if v < 100:
        print("Venda pequena")
    case v if 100 <= v < 500:
        print("Venda média")
    case v if v >= 500:
        print("Venda grande")
# --------------------------------------------------------



####### Atividade 3
# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Menu de formas de pagamento
opcao = input("""
FORMAS DE PAGAMENTO
1 - Pix  (12% de desconto)
2 - Débito  (8% de desconto)
3 - Crédito  (5% de desconto)
4 - Dinheiro  (15% de desconto)
Escolha a opção: """)

desconto = 0

match opcao:
    case "1":
        desconto = valor * 0.12
        print("\n--- Pagamento via PIX ---")

    case "2":
        desconto = valor * 0.08
        print("\n--- Pagamento no Débito ---")

    case "3":
        desconto = valor * 0.05
        print("\n--- Pagamento no Crédito ---")

    case "4":
        desconto = valor * 0.15
        print("\n--- Pagamento em Dinheiro ---")

    case _:
        print("\nOpção inválida.")


if desconto != 0:
    valor_final = valor - desconto
    print(f"Preço normal: R$ {valor:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {valor_final:.2f}")
else:
    print('Escolha uma das opções informadas acima.')
# ---------------------------------------------------------------------