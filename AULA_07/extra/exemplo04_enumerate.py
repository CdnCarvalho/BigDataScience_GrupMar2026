# Criando a lista com as previsões do tempo para cada dia da semana
'''
• Segunda: Nublado
• Terça: Chuvoso
• Quarta: Tempestade
• Quinta: Ensolarado
• Sexta: Ensolarado
'''
# Lista que contém as previsões do tempo para os 5 dias da semana
previsoes_tempo = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]

# Lista com os dias da semana correspondentes às previsões de tempo
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

# Exibindo as duas listas para conferir as previsões e os dias da semana
print(previsoes_tempo)
print(dias_semana)

# Criando listas vazias para armazenar os dias ensolarados e os dias sem sol
dias_ensolarados = []
dias_sem_sol = []

# Percorrendo as previsões de tempo e associando os dias da semana
# Utilizando a função enumerate para obter tanto o índice quanto o valor das previsões
for i, d in enumerate(previsoes_tempo):
    # Se a previsão do tempo for 'Ensolarado', adiciona o dia correspondente
    # na lista dias_ensolarados
    # 'i' é o índice, ou seja, a posição do elemento na lista.
    # 'd' é a previsão do tempo, ou seja, literalmente o conteúdo, que está
    # armazenado no índice atual
    if previsoes_tempo[i] == 'Ensolarado':
        # Método append() é o método que adiciona algo em uma lista, no caso, 
        # o dia da semana na posição atual, ou seja, o dia da semana que está
        # na posição 'i' da lista dos dias_ensolarados
        dias_ensolarados.append(dias_semana[i])
    else:
        # Se a previsão não for 'Ensolarado', usa o método append() para
        # adicionar o dia atual, ou seja, o dia na posição 'i',
        # na lista dias_sem_sol
        dias_sem_sol.append(dias_semana[i])

# Exibindo os dias da semana com previsão ensolarada e sem sol
print("Dias ensolarados: ", dias_ensolarados)
print("Dias sem sol: ", dias_sem_sol)
