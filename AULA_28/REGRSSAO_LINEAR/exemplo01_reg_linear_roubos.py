import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install scikit-learn
# SciKit-Learn é a principal biblioteca de Machine Learning para Python
# from auxiliar.conexoes import obter_dados_pd


# Constante do Endereço dos dados
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter dados
try:
    print('Obtendo dados de ocorrências...')

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.columns) # exibir o nome de todas as colunas

    print(df_ocorrencias.head())    
    print('Dados obtidos com sucesso!')

except Exception as e:
    print('Erro ao obter dados: ', e)
    exit()


# delimitar somente as variáveis solicitadas e totalizar
try:
    print("inciando a delimitação das variáveis e a totalização...")
    
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # Agrupar e totalizar os roubos e recuperações por CISP no pandas novo   
    df_total_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()    
    print(df_total_veiculos)

    print('Delimitação e totalização concluídas!')
except Exception as e:
    print("Erro ao delimitar o dataframe: ", e)
    exit()


# Correlação dos dados
try:
    print('Analisando dados...')

    # Excluir uma parte de valores extremos
    df_total_veiculos_cut = (
        df_total_veiculos[
            df_total_veiculos['roubo_veiculo'] < np.percentile(df_total_veiculos['roubo_veiculo'], 95)
        ]
    )
   
    df_total_veiculos_cut = (
        df_total_veiculos_cut[
            df_total_veiculos_cut['recuperacao_veiculos'] < np.percentile(df_total_veiculos_cut['recuperacao_veiculos'], 99)
        ]
    )

    # Transformando em Arrays
    array_roubo_veiculo = np.array(df_total_veiculos_cut['roubo_veiculo'])
    array_recuperacao_veiculos = np.array(df_total_veiculos_cut['recuperacao_veiculos'])

    # Calculando a correlação
    correlacao = np.corrcoef(array_roubo_veiculo, array_recuperacao_veiculos)[0, 1]

    print('Correlação: ', correlacao)

except Exception as e:
    print("Erro ao analisar dados: ", e)
    exit()


# Regressão linear Análise Preditiva
try:
    print("Iniciando a regressão linear...")

    # pip install scikit-learn
    # SciKit-Learn é a principal biblioteca de Machine Learning para Python


    # Classe para dividir a distribuição dos dados em treino e teste
    from sklearn.model_selection import train_test_split

    # Dividir os dados em treino e teste
    # Roubo de veículos (X): Variável independente - Utilizo para prever
    # Recuperação de veículos (Y): Variável dependente - Prevista
    # Dividir a distribuição dos dados
    X_train, X_test, y_train, y_test = train_test_split(
        array_roubo_veiculo,
        array_recuperacao_veiculos,
        test_size=0.2, # tamanho do conjunto de teste, logo o treino terá 0.8
        random_state=42
    )
    
    # Importar a classe de normalização
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    # Normalização (padronização) dos dados de Roubo de Veículos (X)
    # Usa-se o método fit_transform para padronizar os dados de treino.
    # O StandardScaler transforma os dados para que:
    # - a média fique próxima de 0
    # - o desvio padrão fique próximo de 1
    # Isso ajuda o algoritmo a trabalhar com variáveis na mesma escala.

    # O método fit_transform calcula a média e o desvio padrão de X_train
    # e aplica a transformação nos próprios dados de treino, geranado de uma (1)
    # matriz de 1 coluna e quantas linhas forem necessárias(-1)
    X_train = scaler.fit_transform(X_train.reshape(-1, 1))
    

    # Dados de teste (X_test)
    # só é necessário replicar a transformação
    # Então, não se usa o método fit_transform
    # usa os mesmos valores de média e desvio padrão que foram calculados
    # no X_train, e aplica a mesma transformação nos dados de X_test.
    X_test = scaler.transform(X_test.reshape(-1, 1))

    # LinearRegression: É responsável por criar o modelo de regressão linear
    from sklearn.linear_model import LinearRegression

    # Criar o modelo linear
    # Criando a fórmula da regressão linear. Ainda não sabemos quanto vale a e b
    # O modelo é onde encontraremos a função y = ax + b
    modelo = LinearRegression()

    # Treinar o modelo com os dados de treino y = ax + b
    # O modelo aprende os melhores valores de a e b, com base nos dados de treino
    # No momento do treino, utilizam-se as variáveis de treino de X e y
    # descobre a melhor reta que passa por esses pontos
    #  "aprende uma fórmula matemática para relacionar o roubo de veículos com
    # a recuperação de veículos"
    modelo.fit(X_train, y_train)


    # R² Score (R2 score): Coeficiente de determinação
    # Avaliando a qualidade do modelo com os dados de teste
    # o resultado varia de 0 a 1
    # Quanto mais perto de 1, melhor foi o aprendizado do modelo
    # Acima de 0.7 é um bom modelo, quanto mais se aproxima de 1, melhor
    # Entre 0.5 e 0.7, é um modelo de qualidade moderada, recomenda-se verificar
    # Abaixo de 0.5, é uma modelo de qualidade duvidosa
    r2_score = modelo.score(X_test, y_test)

    print('R² Score:', r2_score)

    # array com os dados de roubo de veículos para prever a recuperação
    array_roubo_veiculo_pred = np.array([40000, 50000, 60000])

    # Normalizar os dados que serão utilizados para previsão
    array_roubo_veiculo_pred_scaled = scaler.transform(
        array_roubo_veiculo_pred.reshape(-1,1)
    )

    # Prever a recuperação de veículos
    recup_pred = modelo.predict(array_roubo_veiculo_pred_scaled)

    print('Previsão de recuperação de veículos (próximos 3 meses): ', recup_pred)

except Exception as e:
    print("Erro ao realizar a regressão linear: ", e)
    exit()


# avaliação do modelo
try:
    print('Avaliando o modelo de previsões...')

    plt.subplots(2, 2, figsize=(15, 5))
    plt.suptitle('Avaliação do modelo de regressão')

    # posição 1: Gráfico de dispersão entre os arrays
    plt.subplot(2, 2, 1)
    # pip install seaborn
    # import seaborn as sns
    sns.regplot(x=array_roubo_veiculo, y=array_recuperacao_veiculos)
    plt.title('Gráfico de dispersão')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperação de veículos')

    # Posicionar o texto no início do gráfico
    plt.text(min(array_roubo_veiculo),
        max(array_recuperacao_veiculos),
        f'Correlação: {correlacao}',
        fontsize=10
    )


    # posição 2: Gráfico de dispersão entre os dados reais e previsto
    plt.subplot(2, 2, 2)

    # Testar o modelo preditivo nos dados de X_teste
    # Saída na escal original dos dados
    y_pred = modelo.predict(X_test)

    # Retornar os dados de teste para escala real
    X_test = scaler.inverse_transform(X_test)

    # Gráfico de dispersão sem a linha de regressão
    plt.scatter(X_test, y_test, color='blue', label='Dados reais')
    plt.scatter(X_test, y_pred, color = 'red', label='Previsões')

    plt.title('Dados reais x previstos')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperações de veículos')

    plt.legend()


    #posição 3: Resíduos
    plt.subplot(2, 2, 3)

    # RESÍDUOS: Diferença entre valores reais e previstos (y_test - y_pred)
    # análise dos resíduos ajuda a verificar se o modelo está capturando bem
    # os padrões dos dados.  # 
    # Bons modelos têm resíduos próximos de 0.
    # Devem ser distribuídos aleatoriamente.
    # Se tiverem um padrão, o modelo não é confiável
    residuos = y_test - y_pred

    # plotar em gráfico de dispersão
    plt.scatter(y_pred, residuos)

    # adicioanar uma linha constante no 0
    plt.axhline(y=0, color='black', linewidth=2)

    plt.title('Resíduos')
    plt.xlabel('Previsões')
    plt.ylabel('Resíduos')

    # posição 4: dispersão dos valores simulados
    plt.subplot(2, 2, 4)
    

    # Prever os valores de roubo de veículos array_roubo_veiculo_pred
    plt.scatter(array_roubo_veiculo_pred, recup_pred)

    plt.title('Recuperações de veículos simuladas')
    plt.xlabel('Roubo veículo simulado')
    plt.ylabel('Recuperação de veículo prevista')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Erro ao avaliar o modelo: ", e)
    exit()

