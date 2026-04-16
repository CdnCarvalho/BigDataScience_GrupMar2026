# Lista para armazenar as notas dos 5 estudantes
medias = []
QUANTIDADE_ESTUDANTES = 5
# Coletando as notas dos estudantes
for i in range(QUANTIDADE_ESTUDANTES):
    nota1 = float(input(f"\nDigite a nota1 do {i+1}º estudante: "))
    nota2 = float(input(f"Digite a nota2 do {i+1}º estudante: "))
    media = (nota1 + nota2) / 2
    medias.append(media)

# Processando as notas e verificando a média
for i in range(5):
    media = medias[i]
    if media > 7:
        print(f"\nEstudante {i+1}: Média {media} - Aprovado!")
    else:
        print(f"Estudante {i+1}: Média {media} - Reprovado!")