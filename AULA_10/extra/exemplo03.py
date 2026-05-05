# -------------------------------------------------
# Função responsável por calcular a média do aluno
# -------------------------------------------------
def calcular_media():

    try:
        nota1 = float(input("Digite a nota 1 (0 a 10): "))
        nota2 = float(input("Digite a nota 2 (0 a 10): "))
        nota3 = float(input("Digite a nota 3 (0 a 10): "))

        # Validação do intervalo
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
            print("\nErro na digitação!!!: As notas devem estar entre 0 e 10.")
            return

    except (ValueError, TypeError):
        print("\nErro!!!: Digite apenas números.")

    else:
        media = (nota1 + nota2 + nota3) / 3
        print(f"\nMédia final: {media:.2f}")

        if media >= 7:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")

    finally:
        print("\nEncerrando a operação.")
        print("-" * 30)


# --------------------------------------------------------
# Programa principal
# --------------------------------------------------------
print(30 * "=")
print("  Cálculo da Média do Aluno")
print(30 * "=")

calcular_media()
print("\nPrograma finalizado.")
