# ----------------------------------------------------------- Multiplas Exceções - Except, Else e Finally - Exemplo 03 ( Letras, divisão por zero)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except (ValueError, TypeError):
    print("\nErro: informe apenas números válidos.")
except ZeroDivisionError:
    print("\nErro: não há funcionários ativos para calcular a média.")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")
finally:
    print("\nRelatório finalizado.")





# ----------------------------------------------------------- except Exception - Exemplo (Capturando o erro genérico {e})
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except Exception as e:
    print(f"\nErro inesperado: {e}")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")
finally:
    print("\nRelatório finalizado.")