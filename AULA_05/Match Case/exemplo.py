# Recebe o código de acesso digitado pelo usuário
codigo = int(input("Informe o código de acesso: "))

# Verifica a área correspondente com base no código usando match/case
match codigo:
    case 1:
        print("Marketing")
    case 2:
        print("Financeiro")
    case 3 | 4 | 5:
        print("ADM")
    case 6 | 7 | 8 | 9:  # Usando o Pipe no sentido de 6 ou 7
        print("TI")
    case 10:  # Pipe como operador ou 'Or'
        print("Serviços Gerais")
    case _:
        print("Acesso negado.")



# # Recebe o código de acesso digitado pelo usuário
# codigo = int(input("Informe o código de acesso: "))

# # Verifica a área correspondente com base no código usando match/case
# match codigo:
#     case 1:
#         print("Marketing")
#     case 2:
#         print("Financeiro")
#     case codigo if codigo == 3 or codigo == 4 or codigo == 5:
#         print("ADM")
#     case 6 | 7 | 8 | 9:  # Usando o Pipe no sentido de 6 ou 7
#         print("TI")
#     case 10:  # Pipe como operador ou 'Or'
#         print("Serviços Gerais")
#     case _:
#         print("Acesso negado.")



# Recebe o código de acesso digitado pelo usuário
codigo = int(input("Informe o código de acesso: "))

# Verifica a área correspondente com base no código usando match/case
match codigo:
    case 1:
        print("Marketing")
    case 2:
        print("Financeiro")
    case c if 3 <= c <= 5:  # usando if para verificar o intervalo
        print("ADM")
    case c if 6 <= c <= 9:  # usando if para verificar o intervalo
        print("TI")
    case 10: 
        print("Serviços Gerais")
    case _:
        print("Acesso negado.")

# --------------------------------------------------------
###### Exemplo 2
# Classificando idade
print("""
CLASSIFICAÇÃO POR IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos ou menos
""")

idade = int(input("Digite a idade: "))

match idade:
    case i if 0 <= i < 12:
        print("Criança")
    case i if 12 <= i < 18:
        print("Adolescente")
    case i if i >= 18:
        print("Adulto")
    case _:
        print("Idade inválida.")


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


###### Atividade 2
valor = float(input("Digite um valor de venda: "))

match valor:
    case v if 0 <= v < 100:
        print("Sem Bônus")
    case v if 100 <= v < 500:
        print("Bônus de 5%")
    case v if v >= 500:
        print("Bônus de 10%")
# --------------------------------------------------------



####### EXEMPLO 3
# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Menu de formas de pagamento
print("""
FORMAS DE PAGAMENTO
1 - Pix  (12% de desconto)
2 - Débito  (8% de desconto)
3 - Crédito  (5% de desconto)
4 - Dinheiro  (15% de desconto)
""")

opcao = input("Escolha a opção: ")

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
