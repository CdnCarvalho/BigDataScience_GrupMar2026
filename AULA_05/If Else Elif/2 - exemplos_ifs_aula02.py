
# IFs encadeados (com ELIF)
nota = 10 
if nota >= 7:
    print("Aluno aprovado")
elif nota >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")

# -----------------------------------------------------------
# Explicar a diferença entre IFs independentes e IFs encadeados (com ELIF)
nota = 10 
if nota >= 9:
    print("Conceito A")

if nota >= 7:
    print("Conceito B")

if nota >= 5:
    print("Conceito C")

if nota >= 3:
    print("Conceito D")
else:
    print("Conceito E")

# -----------------------------------------------------------


############### IFS ENCADEADOS ##############
# EXEMPLO 6 - IF dentro de IF (aninhado)
# Enunciado: Verifique se o aluno passou de ano e se teve boa frequência.
nota = float(input("Digite a média final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if nota >= 7:
    if frequencia >= 75:
        print("Aluno aprovado com bom desempenho e boa frequência.")
    else:
        print("Aluno com boa nota, mas reprovado por falta.")
else:
    print("Aluno reprovado por nota baixa.")
# -----------------------------------------------------------


# EXEMPLO 7 - IF dentro de IF (aninhado com alternativa no ELSE)
# Enunciado: Verifique se o cliente pode parcelar a compra e qual será o número máximo de parcelas.
valor_compra = float(input("Digite o valor total da compra: "))

if valor_compra >= 100:
    print("Compra elegível para parcelamento.")
    if valor_compra > 500:
        valor_parcela = valor_compra / 10
        print(f"Você pode parcelar em até 10x de R$ {valor_parcela:.2f} sem juros.")
    else:
        valor_parcela = valor_compra / 5
        print(f"Você pode parcelar em até 5x de  R$ {valor_parcela:.2f} sem juros.")
else:
    print("Valor abaixo do mínimo para parcelamento.")
# -----------------------------------------------------------
