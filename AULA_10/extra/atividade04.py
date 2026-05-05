print('Sistema de Cálculo de Média Escolar')

try:
    # Tentativa de entrada das duas notas
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

except Exception as e:
    # Captura qualquer erro de entrada (ex: texto ao invés de número)
    print(f'Erro: {e.__class__.__name__} - Digite apenas números válidos.')

else:
    # Se as entradas forem válidas, verifica o intervalo
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f'Média do aluno: {media:.2f}')
        if media >= 6:
            print('Aluno aprovado!')
        else:
            print('Aluno reprovado.')
    else:
        print('As notas devem estar entre 0 e 10.')

finally:
    # Mensagem final, mesmo se houve erro
    print('Operação Finalizada')
