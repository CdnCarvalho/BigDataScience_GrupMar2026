# Lista para armazenar os candidatos válidos
candidatos = []

# Cadastro de 5 pessoas
for i in range(5):
    print(f"\nCadastro da {i+1}ª pessoa:")

    candidato = {}

    candidato['nome'] = input("Nome: ")
    candidato['data_nascimento'] = input("Data de nascimento: ")
    candidato['telefone'] = input("Telefone: ")
    candidato['email'] = input("E-mail: ")
    candidato['formacao'] = input("Formação acadêmica: ")

    # Entrada da idade para validação
    idade = int(input("Idade: "))

    # Estrutura de decisão
    if idade >= 18:
        candidatos.append(candidato)
        print("Candidato cadastrado com sucesso!")
    else:
        print("Candidato menor de idade. Cadastro não permitido.")

# Exibe os candidatos válidos
print("\n--- CANDIDATOS CADASTRADOS ---")
for c in candidatos:
    print(c)