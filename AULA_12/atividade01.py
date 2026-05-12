import pandas as pd

# Listas com categorias e quantidades totais de livros
categorias = ["Literatura Brasileira", "Literatura Estrangeira", "Ciências", "Matemática", "História"]
estoque = [12, 9, 18, 14, 20]

# Lista com a quantidade de livros emprestados por categoria
emprestados = [4, 2, 7, 5, 6]

# Conversão das listas em séries
estoque_total = pd.Series(estoque, index=categorias)
emprestados_series = pd.Series(emprestados, index=categorias)

# Adição da nova categoria Filosofia com valor ausente
estoque_total["Filosofia"] = None
emprestados_series["Filosofia"] = None

# Cálculo dos livros disponíveis
disponiveis = estoque_total - emprestados_series
print(disponiveis)


# Filtrando categorias com mais de 5 livros disponíveis
mais_de_10_disponiveis = disponiveis[disponiveis > 10]

# Exibição dos dados filtrados
print("\nCategorias com mais de 5 livros disponíveis para empréstimo:")
print(mais_de_10_disponiveis)
