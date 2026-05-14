import numpy as np

idade = np.array([35, 18, 22, 48, 25, 38, 52, 31, 45, 22, 36, 33, 23, 56, 29, 40, 32, 20])
# [18 20 22 22 23 25 29 31 32 33 35 36 38 40 45 48 52 56]

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)

print('Primeiro quartil (Q1): ', q1)
print('Segundo quartil (Q2): ', q2)
print('Terceiro quartil (Q3): ', q3)

# A média te diz: “A idade média é X” 
# Os quartis dizem: “Onde estão os grupos, as faixas da sua distribuição”