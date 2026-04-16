# ----------------------------------------------------------
# ATIVIDADE 01 - LISTA DE CANDIDATOS
candidatos = []

# Coleta dos dados
for i in range(5):
    print(f"\nCadastro do {i+1}º candidato:")

    candidato = {}

    candidato['nome'] = input("Nome completo: ")
    candidato['idade'] = int(input("Idade: "))
    candidato['telefone'] = input("Telefone: ")
    candidato['email'] = input("E-mail: ")
    candidato['formacao'] = input("Formação acadêmica: ")

    candidatos.append(candidato)
    print("Cadastro realizado com sucesso.")

# Exibe todos os candidatos
print("\nLista de candidatos:")
for c in candidatos:
    print(c)
# ----------------------------------------------------------



# ATIVIDADE 01 - LISTA DE CANDIDATOS  # While True 
candidatos = []

contador = 1

# Coleta dos dados
while True:
    print(f"\nCadastro do {contador}º candidato:")

    candidato = {}

    candidato['nome'] = input("Nome completo: ")
    candidato['idade'] = int(input("Idade: "))
    candidato['telefone'] = input("Telefone: ")
    candidato['email'] = input("E-mail: ")
    candidato['formacao'] = input("Formação acadêmica: ")

    candidatos.append(candidato)
    print("Cadastro realizado com sucesso.")

    contador += 1

    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro candidato? (s/n): ").lower()
    
    if continuar == "n":
        break

# Exibe todos os candidatos
print("\nLista de candidatos:")
for c in candidatos:
    print(c)

# --------------------------------------------------------------------------



# Atividade 02 - Vendas maior ou igual a Meta 5000
# Lista para armazenar os vendedores
vendedores = []

# Cadastro de 3 vendedores
for i in range(3):
    print(f"\nCadastro do {i+1}º vendedor:")

    vendedor = {}

    vendedor['nome'] = input("Nome: ")
    vendedor['regiao'] = input("Região: ")
    vendedor['vendas'] = float(input("Valor total de vendas no mês: "))
    vendedor['quantidade'] = int(input("Quantidade de vendas: "))

    vendedores.append(vendedor)
    print("Vendedor cadastrado com sucesso!")

# Mostra apenas vendedores que atingiram a meta
print("\n--- VENDEDORES QUE ATINGIRAM A META ---")
for vendedor in vendedores:
    if vendedor['vendas'] >= 5000:
        print(vendedor)




