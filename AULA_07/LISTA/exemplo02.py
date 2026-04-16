# LISTA PARA ARMAZENAR 5 NÚMEROS
lista_produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']


# Mostrando os dados
print(f"\nLista Inicial: {lista_produtos}")


# Alterando o primeiro número da lista
lista_produtos[0] = "PC Desktop"
print("Lista Alterada:", lista_produtos)

# Adicionando um novo número
lista_produtos.append("Webcam")
print("Novo produto adicionado:", lista_produtos)

# Removendo um número
lista_produtos.remove("Monitor")  # só remove se o número existir
print("Lista após Remoção:", lista_produtos)

# Removendo o último número
lista_produtos.pop()
print("Remoção do Último:", lista_produtos)

# Removendo pelo índice
del lista_produtos[0]
print("Lista Removendo pelo índice:", lista_produtos)

# Limpando a lista
lista_produtos.clear()
print(lista_produtos)


# Exemplo 02.1 (Replicar no exemplo 01)
# For sem range()
for produto in lista_produtos:
    print(f"Produto: {produto}")