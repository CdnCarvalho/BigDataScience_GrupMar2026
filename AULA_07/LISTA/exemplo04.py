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