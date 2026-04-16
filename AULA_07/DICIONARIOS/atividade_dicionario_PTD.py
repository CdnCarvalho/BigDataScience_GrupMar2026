# Lista para armazenar os candidatos válidos
candidatos = []

# Cadastro de 5 pessoas
for i in range(5):
    print(f"\nCadastro da {i+1}ª pessoa:")

    idade = int(input("Idade: "))

    if idade >= 18:
        # Só entra aqui se for maior de idade
        candidato = {}

        candidato['nome'] = input("Nome: ")
        candidato['data_nascimento'] = input("Data de nascimento: ")
        candidato['telefone'] = input("Telefone: ")
        candidato['email'] = input("E-mail: ")
        candidato['formacao'] = input("Formação acadêmica: ")

        candidatos.append(candidato)
        print("Candidato cadastrado com sucesso!")
    else:
        print("Candidato menor de idade. Não pode se candidatar.")


# Exibe os candidatos válidos
print("\n--- CANDIDATOS CADASTRADOS ---")
for c in candidatos:
    print(c)