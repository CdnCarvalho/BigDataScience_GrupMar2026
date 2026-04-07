# ATIVIDADE 01
# Sistema simples para aplicar desconto em compras acima de R$ 250,00

# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Verificação da condição para aplicar o desconto
if valor > 250:
    desconto = valor * 0.16  # Calcula 16% de desconto
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")



# --------------------------------------------------------------------------
# ATIVIDADE 02
# Entrada dos dados
valor = float(input("Informe o valor da compra: R$ "))
forma_pagamento = input("Informe a forma de pagamento (à vista ou parcelado): ")

# Padronizando o texto para evitar erro de digitação
forma_pagamento = forma_pagamento.lower()

# Verificação das duas condições ao mesmo tempo
if valor > 250 and forma_pagamento == "à vista":
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")



# ---------------------------------------------------------------------------


#########  EXTRAS  #########

# ATIVIDADE 03
# Sistema para verificar se um pedido pode ser enviado

# Entrada de dados
estoque = int(input("Informe a quantidade em estoque: "))
solicitado = int(input("Informe a quantidade solicitada no pedido: "))
peso = float(input("Informe o peso total do pedido (em kg): "))

# Verificação das duas condições ao mesmo tempo (AND)
if estoque >= solicitado and peso <= 50:
    print("Pedido liberado para envio.")
else:
    print("Pedido não pode ser enviado. Verifique a quantidade em estoque e/ou o peso do pedido.")

# ---------------------------------------------------------------------------

# ATIVIDADE 04
# Sistema para verificar se um cooperado/a tem acesso ao benefício

# Entrada de dados
tempo_filiacao = int(input("Informe o tempo de filiação (em anos): "))
valor_movimentado = float(input("Informe o valor movimentado nos últimos 6 meses (em R$): "))

# Verificação de pelo menos uma condição verdadeira (OR)
if tempo_filiacao > 3 or valor_movimentado > 5000:
    print("Você tem direito ao benefício especial da cooperativa.")
else:
    print("Você ainda não atende aos critérios para o benefício.")

# --------------------------------------------------------------------------------------------------


# ATIVIDADE 1 – Validação de Qualidade dos Dados (If / Elif / Else)

# Enunciado:
# Você está ajudando um analista de dados a validar informações recebidas em um arquivo.
# O analista quer saber, se um valor numérico fornecido pelo usuário é considerado:
# Inválido
# Baixo
# Aceitável
# Alto

# As regras são:
# Valores menores que 0 → “Valor inválido.”
# Valores entre 0 e 50 → “Valor considerado BAIXO.”
# Valores entre 51 e 200 → “Valor ACEITÁVEL.”
# Valores acima de 200 → “Valor ALTO. Pode indicar um erro no dado.”
# Crie um programa que receba um número e mostre a mensagem correta.
valor = float(input("Digite o valor numérico para verificação: "))

if valor < 0:
    print("Valor inválido.")
elif valor <= 50:
    print("Valor considerado BAIXO.")
elif valor <= 200:
    print("Valor ACEITÁVEL.")
else:
    print("Valor ALTO e pode indicar um erro no dado.")



# ATIVIDADE 2 – Sistema de Frete com Mais Categorias (If / Elif / Else)
# Enunciado:

# Uma loja online aplica diferentes valores de frete conforme o total da compra.
# As regras são:
# Compras acima de R$ 500,00 → frete GRÁTIS
# Compras entre R$ 300 e R$ 500 → frete R$ 10,00
# Compras entre R$ 150 e R$ 299 → frete R$ 20,00
# Compras entre R$ 80 e R$ 149 → frete R$ 30,00
# Compras abaixo de R$ 80 → frete R$ 45,00

# Crie um programa que receba o valor da compra e mostre qual frete deve ser aplicado.
valor = float(input("Digite o valor total da compra: R$ "))

if valor > 500:
    print("Frete GRÁTIS.")
elif valor >= 300:
    print("Frete de R$ 10,00.")
elif valor >= 150:
    print("Frete de R$ 20,00.")
elif valor >= 80:
    print("Frete de R$ 30,00.")
else:
    print("Frete de R$ 45,00.")

