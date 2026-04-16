# criar o conjunto de previsões tempo
# Em python, temos uma estrtura de dados chamada LISTA
# A lista é uma coleção mutável.
# As listas são recomendadas p/ armazenar conjunto de itens ou seja,
# conjunto de dados.
# AS listas podem receber qualquer tipo de dados, int, floats, bool,
# strigs e inclusive, podem receber variáveis, e até mesmo outras listas.
# As Listas podem interagir com outras listas, desde que faça sentido.
# Podem armazenar arquivos, como excel, csv, tabelas de banco de dados etc.
# Existe uma boa prática para nomenclatura listas: 
# snake_case
# nomes no plural
# É opcional: iniciar com o prefixo lst_
# A lista é representada pelos colchetes [ ]

previsoes_tempo = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]

# Exibir a lista
print(previsoes_tempo)

PREVISAO_FELIZ = "Ensolarado"

# Percorrer os itens da lista e verificar, se o valor do item é 'Ensolarado'
# Para percorrer essa lista, utilizaremos nesse momento
# O LAÇO de repetição "FOR".
# Ao usar o laço for, Lê-se a estrutura desta forma: (Para cada item, faça ...)
# No funcionamento do laço for, uma variável temporária da própria estrutura, 
# armazena cada um dos valores da lista, a cada iteração.
# Assim, para cada valor da lista, o bloco de comando do for será executado.
# 
# Exemplo de sintaxe:
# for <variável temporária da própria estrutura> in [lista_com_os_itens]:

# Loop sobre a lista previsoes_tempo
for previsao in previsoes_tempo:
    # Na primeira rodada, a variável "previsao" já armazenará o
    # primeiro item da lista
    print(previsao)
    
    # Verifica, se a previsão do tempo é igual a 'PREVISAO_FELIZ'
    if previsao == PREVISAO_FELIZ:
        # Se a previsão for 'PREVISAO_FELIZ', o algortmo entra no IF
        # e executa a linnha do print, impriminfo uma mensagem positiva
        print(f"O dia será {previsao}. Aproveite para passear.")
    else:
        # Se a previsão, não for 'PREVISAO_FELIZ', imprime uma mensagem
        # sobre 'guarda-chuva'
        print(f"O dia será {previsao}. Não esqueça o guarda-chuva.")