# -------------------------------------------------- Soma apenas,
#  se ambos os números forem pares
def somar_pares(a, b):
    if a % 2 != 0 or b % 2 != 0:
        return "Não calculado: números ímpares informados"
    
    return a + b


print("=== Soma de números pares ===")

for i in range(3):
    print(f"\nPar {i+1}")

    try:
        n1 = int(input("Digite o primeiro número par: "))
        n2 = int(input("Digite o segundo número par: "))

    except ValueError:
        print("Erro: informe apenas números inteiros.")
    except KeyboardInterrupt:
        print("Erro: operação interrompida pelo usuário.")

    else:
        resultado = somar_pares(n1, n2)
        print(f"Resultado do {i+1}º par: {resultado}")

    finally:
        print("Operação encerrada.")
