# ------------------------------------------------------------------------
# dicionario = {} => Cria vazio
# dicionario["chave"] = valor => Adiciona/Modifica
# print(dicionario["chave"]) => Acessa valor
# del dicionario["chave"] => Remove item
# dicionario.clear() => Limpa tudo dentro do dicionário
# ------------------------------------------------------------------------

# criando um dicionário com produtos e seus preços
# criando um dicionário com dados de uma pessoa
pessoa = {}

pessoa["nome"] = "João"
pessoa["idade"] = 25
pessoa["cidade"] = "Niterói"

print(pessoa)  # mostrando o dicionário

# acessando uma chave específica
print(pessoa["nome"])  # nome da pessoa

# alterando o valor de uma chave
pessoa["idade"] = 26

# adicionando uma nova informação
pessoa["profissao"] = "Programador"

# removendo uma informação
del pessoa["cidade"]

print(pessoa)


#  ------------------------------------------------------------------------
# EXEMPLO 02 - DICIONÁRIO AMIGOS
amigo = {}  # Dicionário vazio

# Adicionando amigos com suas idades
amigo["Nome"] = "Pedro"
amigo["Tel"] = '2298521-2541'
amigo["Email"] = 'maria@gmail.com'

print(amigo)

print("Telefone de Pedro:", amigo["Tel"])  # Acessando pela chave

# alterndo uma chave
amigo["Tel"] = "2298888-8888"

# Adicionando nova chave
amigo["Cidade"] = "Niterói"

# Removendo uma chave
del amigo["Email"]

print("Todos os amigos:", amigo)




# ------------------------------------------------------------------------
# Exemplo 02
# Lista para armazenar os livros
livros = []

# Cadastro de 3 livros
for i in range(3):
    print(f"\nCadastro do {i+1}º livro:")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    genero = input("Gênero: ")
    paginas = int(input("Número de páginas: "))

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'genero': genero,
        'paginas': paginas
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Mostra apenas livros a partir de 2020
print("\n--- LIVROS A PARTIR DE 2020 ---")
for livro in livros:
    if livro['ano'] >= 2020:
        print(livro)


# -------------------------------------------------------------------------------
# Exemplo 02 - Lista para armazenar os livros - while True
# Lista para armazenar os livros
livros = []
contador = 1

# Cadastro de livros
while True:
    print(f"\nCadastro do {contador}º livro:")

    livro = {}

    livro['titulo'] = input("Título: ")
    livro['autor'] = input("Autor: ")
    livro['ano'] = int(input("Ano de publicação: "))
    livro['genero'] = input("Gênero: ")
    livro['paginas'] = int(input("Número de páginas: "))

    livros.append(livro)
    print("Livro cadastrado com sucesso!")

    contador += 1

    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
    
    if continuar == "n":
        break

# Mostra apenas livros a partir de 2020
print("\n--- LIVROS A PARTIR DE 2020 ---")
for livro in livros:
    if livro['ano'] >= 2020:
        print(livro)