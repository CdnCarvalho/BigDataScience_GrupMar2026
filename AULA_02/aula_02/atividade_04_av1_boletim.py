# recebe 4 notas, calcula a média e mostra se o aluno foi aprovado ou reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica se o aluno foi aprovado ou reprovado
# se a média for maior ou igual a 7, o aluno foi aprovado,
# se a média for entre 5 e 7, o aluno está de recuperação,
# se a média for menor que 5, o aluno foi reprovado
if media >= 7:
    print("Aluno aprovado com média", media)
elif media >= 5 and media < 7:
    print("Aluno em recuperação com média", media)
else:
    print("Aluno reprovado com média", media)
