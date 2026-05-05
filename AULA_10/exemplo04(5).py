# ======================================
# ####### FUNÇÃO - cálculo de média

# Esta função recebe uma lista de notas
# Ela calcula a soma de todas as notas e a média
def calcular_media(lista_notas):
    total = sum(lista_notas)           # soma todas as notas
    media = total / len(lista_notas)   # divide pela quantidade de notas
    return total, media               # retorna os dois valores


# -------------------------------------
# PROGRAMA PRINCIPAL

contador = 1  # controle de alunos

while True:
    print('\n' + 30 * '=')
    print(f'ALUNO {contador}')

    # entrada de dados
    aluno = input('Informe o nome do aluno: ')

    notas = []  # lista para armazenar as 4 notas

    # -------------------------------------
    # COLETA DAS NOTAS COM TRATAMENTO DE ERRO

    try:
        # o range(4) garante que serão solicitadas exatamente 4 notas
        for i in range(4):
            # Pode gerar erro se o usuário não digitar número
            nota = float(input(f'Informe a nota {i+1}: '))
            notas.append(nota)  # adiciona a nota na lista

    except ValueError:
        # Executa se o usuário digitar algo inválido
        print('Erro: informe apenas valores numéricos para as notas.')

    else:
        # Executa somente se NÃO houver erro

        # chamada da função
        # enviamos a lista de notas para calcular o total e a média
        total, media = calcular_media(notas)

        # saída de dados
        print('\nRESULTADO:')
        print(f'Aluno: {aluno}')
        print(f'Soma das notas: {total:.2f}')
        print(f'Média final: {media:.2f}')

        # EXTRA
        print(f'Notas informadas: {notas}')           # todas as notas
        print(f'Maior nota: {max(notas):.2f}')        # maior nota
        print(f'Menor nota: {min(notas):.2f}')        # menor nota

    finally:
        # Sempre executa, independente de erro
        print('Processo finalizado para este aluno.')

    # -------------------------------------
    # CONTROLE DE REPETIÇÃO

    opcao = input('\nDeseja cadastrar outro aluno? (S/N): ').strip().upper()

    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')