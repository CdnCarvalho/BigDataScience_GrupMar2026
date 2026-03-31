# EXEMPLO 1 - IF / ELSE básico
# Enunciado: Verifique se a pessoa é maior de idade.
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# -----------------------------------------------------------


# EXEMPLO 2 - IF com ELIF
# Enunciado: Verifique a faixa de pontuação de um jogador.
pontos = int(input("Digite sua pontuação: "))

if pontos >= 100:
    print("Excelente! Você atingiu o nível máximo.")
elif pontos >= 50:
    print("Bom desempenho! Continue jogando.")
else:
    print("Você está começando. Pratique mais!")
# -----------------------------------------------------------


# EXEMPLO 3 - IF com operador AND
# Enunciado: Verifique se o usuário pode realizar o login.
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha incorretos.")
# -----------------------------------------------------------


# EXEMPLO 4 - IF com operador OR
# Enunciado: Verifique se o dia é fim de semana.
# tirar os espaços em branco e colocar tudo em minúsculo para evitar erros de digitação
dia = input("Digite o dia da semana: ").lower().strip()

if dia == "sábado" or dia == "domingo":
    print("É fim de semana! Aproveite o descanso.")
else:
    print("Dia útil! Hora de trabalhar ou estudar.")
# -----------------------------------------------------------


# EXEMPLO 5 - Combinação de condições com AND e OR
# Enunciado: Verifique se o cliente tem direito a um brinde.
compra = float(input("Digite o valor da compra: "))
cliente_frequente = input("O cliente é cadastrado no programa de fidelidade? (s/n): ").lower()

if compra > 100 or cliente_frequente == "s":
    print("Cliente tem direito a um brinde!")
else:
    print("Sem brinde desta vez.")
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
        print("Você pode parcelar em até 10x sem juros.")
    else:
        print("Você pode parcelar em até 5x sem juros.")
else:
    print("Valor abaixo do mínimo para parcelamento.")
# -----------------------------------------------------------
