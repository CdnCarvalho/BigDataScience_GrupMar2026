# lista vazia para armazenar as vendas
vendas = []

# cadastrando 10 vendas
for i in range(3):
    valor = float(input(f"Digite o valor da venda {i+1}: "))
    vendas.append(valor)

# exibir lista de vendas
print("\nLista de vendas:", vendas)

# definição de constantes
META = 1000
META_MINIMA = 700

# Percorrer a lista de vendas
for venda in vendas:
    if venda >= META:
        print(f"A venda foi de R${venda}. Meta atingida!")
    elif venda >= META_MINIMA and venda < META:
        print(f"A venda foi de R${venda}. Próximo da meta.")
    else:
        print(f"A venda foi de R${venda}. Abaixo da meta.")



# Exemplo01 - Alterar para While True
# lista vazia para armazenar as vendas
vendas = []
contador = 1

# cadastrando vendas (quantidade indefinida)
while True:
    valor = float(input(f"Digite o valor da venda {contador}: "))
    vendas.append(valor)

    contador += 1

    # pergunta se deseja continuar
    continuar = input("Deseja cadastrar outra venda? (s/n): ").lower()
    
    if continuar == "n":
        break

# exibir lista de vendas
print("\nLista de vendas:", vendas)

# definição de constantes
META = 1000
META_MINIMA = 700

# Percorrer a lista de vendas
for venda in vendas:
    if venda >= META:
        print(f"A venda foi de R${venda}. Meta atingida!")
    elif venda >= META_MINIMA and venda < META:
        print(f"A venda foi de R${venda}. Próximo da meta.")
    else:
        print(f"A venda foi de R${venda}. Abaixo da meta.")