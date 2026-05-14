# Importa a biblioteca NumPy
# Útil para operações numéricass de forma rápida e eficiente
# Permite manipulação de vetores "arrays"
import numpy as np  

# Lista de salários em uma moeda fictícia, representando uma pequena amostra de dados com um valor atípico (30000)
dados_salario = [3000, 2500, 4000, 3500, 2000, 30000]

# Calcula a média aritmética dos salários
# A média é sensível a valores atípicos, então o valor alto (30000) influencia este cálculo
media = np.mean(dados_salario)

# Calcula a mediana dos salários
# A mediana é o valor central. Não sofre grande influência de valores extremos, 
# sendo útil para representar a posição central quando há valores atípicos
mediana = np.median(dados_salario)

# Exibe a média e a mediana
print('Média: ', media)       # Mostra o valor da média calculada
print('Mediana: ', mediana)    # Mostra o valor da mediana calculada


q1 = np.quantile(dados_salario, 0.25)
q2 = np.quantile(dados_salario, 0.50)
q3 = np.quantile(dados_salario, 0.75)
print(q1, q2, q3)