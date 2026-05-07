# Criar um dataset de 3 colunas coma as seguintes informações: 
# nome do filme; ano de lançamento e gênero. 

import pandas as pd

# dicionário com informações dos filmes
filmes = {
    'titulo': ["Avatar", "Vingadores", "Titanic"],
    'lançamento': [2009, 2012, 1997],
    'genero': ["Ficção", "Ação", "Romance"]
}

# transformando o dicionário em DataFrame
df_filmes = pd.DataFrame(filmes)

# exibindo o DataFrame
print(df_filmes)

