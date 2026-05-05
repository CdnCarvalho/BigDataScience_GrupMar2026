# Função para somar dois números
def somar(sal, bon):
    return sal + bon


print("=== BONIFICAÇÃO NO SALÁRIO ===")

# Loop para 3 repetições
for i in range(3):
    print(f"\n--- Operação {i+1} ---")

    try:
        salario = float(input("Salário: "))
        bonus = float(input("Bonus: "))

    except ValueError:
        print("Erro Informe apenas números")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
    else:
        # Executa somente se NÃO ocorrer erro
        resultado = somar(salario, bonus)
        print(f"Total do Salário: {resultado}")

    finally:
        # Executa sempre, com erro ou sem erro
        print("Operação finalizada.")

print("\nPrograma encerrado." )



