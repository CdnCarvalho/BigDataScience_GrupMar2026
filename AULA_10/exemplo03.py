
############### ESTRUTURAS DE REPETIÇÃO, FUNÇÕES E EXCEÇÕES ###############
# -------------------------------------------------- EXEMPLO - Função Percentual de atingimento de metas (3 funcionários)
# ####### FUNÇÃO - cálculo de atingimento
def calcula_atingimento(n1, n2):
    result = n1 / n2
    return result * 100



contador = 1  # controle de vendedor

while True:
    try:
        # ENTRADA DE DADOS
        vendas = float(input(f"Digite o total de venda do vendedor {contador}: "))
        meta = float(input("Digite o valor da meta: "))

        # CHAMADA DA FUNÇÃO
        resultado = calcula_atingimento(vendas, meta)

    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Erro!!!: Digite apenas dados numéricos para as vendas e meta.")

    except ZeroDivisionError:
        # Caso a meta seja zero (divisão por zero)
        print("Erro!!!: A meta não pode ser zero.")

    else:
        # Executa somente se não houver erro
        print(f"Percentual de atingimento do vendedor {contador}: {resultado:.2f}%")

    finally:
        # Sempre executa
        print(f"Cálculo do vendedor {contador} finalizado.\n")


    # -------------------------------------
    # CONTROLE DE REPETIÇÃO

    opcao = input("Deseja calcular outro vendedor? (S/N): ").strip().upper()

    if opcao != 'S':
        break

    contador += 1


print("Programa encerrado!")



