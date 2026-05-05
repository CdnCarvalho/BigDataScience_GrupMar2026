# ----------------------------------------------------------- Except - Exemplo 01 (Explicação 1: Letras ao invés de números)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios
    print(f"\nMédia produzida por funcionário: {media_por_funcionario:.2f}")
except ValueError:
    print(f"\nErro: informe apenas números.")




# ----------------------------------------------------------- Except Else - Exemplo 02  Letras ao invés de números)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios
    print(f"\nMédia produzida por funcionário: {media_por_funcionario:.2f}")

except ValueError:
    print("\nErro: informe apenas números válidos.")
except ZeroDivisionError:
    print("\nErro: não é possível dividir por zero.")




# TRY NA PRÁTICA
# ----------------------------------------------------------- Estrutura de repetição - SEM TRY
# NA PRÁTICA
# Exemplo: Para 05 funcionários:
for i in range(5):
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios
    print(f"\nMédia produzida por funcionário: {media_por_funcionario:.2f}")



# ----------------------------------------------------------- TRY - EM ESTRUTURA DE REPETIÇÃO
# NA PRÁTICA: Para o programa não quebrar
for i in range(5):
    try:
        total_produzido = float(input("Informe o total produzido no mês: "))
        funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

        media_por_funcionario = total_produzido / funcionarios
        print(f"\nMédia produzida por funcionário: {media_por_funcionario:.2f}")

    except ValueError:
        print("\nErro: informe apenas números válidos.")
    except ZeroDivisionError:
        print("\nErro: não é possível dividir por zero.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")


