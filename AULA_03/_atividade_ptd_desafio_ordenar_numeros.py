# imprimir os números em ordem crescente

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 and n1 < n3:
    menor = n1
    if n2 < n3:
        meio = n2
        maior = n3
    else:
        meio = n3
        maior = n2

elif n2 < n1 and n2 < n3:
    menor = n2
    if n1 < n3:
        meio = n1
        maior = n3
    else:
        meio = n3
        maior = n1

else:
    menor = n3
    if n1 < n2:
        meio = n1
        maior = n2
    else:
        meio = n2
        maior = n1

print("Os números em ordem crescente são:", menor, meio, maior)






# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# # Verificação se todos são iguais
# if n1 == n2 == n3:
#     print("Os números são iguais:", n1, n2, n3)

# else:
#     # Verifica se dois são iguais
#     if n1 == n2 and n1 < n3:
#         menor = meio = n1
#         maior = n3
#     elif n1 == n3 and n1 < n2:
#         menor = meio = n1
#         maior = n2
#     elif n2 == n3 and n2 < n1:
#         menor = meio = n2
#         maior = n1

#     elif n1 == n2 and n1 > n3:
#         menor = n3
#         meio = maior = n1
#     elif n1 == n3 and n1 > n2:
#         menor = n2
#         meio = maior = n1
#     elif n2 == n3 and n2 > n1:
#         menor = n1
#         meio = maior = n2

#     # Caso todos sejam diferentes
#     elif n1 < n2 and n1 < n3:
#         menor = n1
#         if n2 < n3:
#             meio = n2
#             maior = n3
#         else:
#             meio = n3
#             maior = n2

#     elif n2 < n1 and n2 < n3:
#         menor = n2
#         if n1 < n3:
#             meio = n1
#             maior = n3
#         else:
#             meio = n3
#             maior = n1

#     else:
#         menor = n3
#         if n1 < n2:
#             meio = n1
#             maior = n2
#         else:
#             meio = n2
#             maior = n1

#     print("Os números em ordem crescente são:", menor, meio, maior)