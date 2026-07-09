import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # df_total_lesoes = df_lesoes.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_morte']).reset_index()
    
    # Agrupando por CISP e totalizando as lesões
    df_total_lesoes = df_lesoes.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    print(df_total_lesoes.head())

    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# correlação
try:
    print('Calculando a correlação...')

    df_total_lesoes_cut = df_total_lesoes[df_total_lesoes['lesao_corp_morte'] < np.percentile(df_total_lesoes['lesao_corp_morte'], 95)] 
    df_total_lesoes_cut = df_total_lesoes_cut[df_total_lesoes_cut['lesao_corp_dolosa'] < np.percentile(df_total_lesoes_cut['lesao_corp_dolosa'], 99)]

    array_dolosa = np.array(df_total_lesoes_cut['lesao_corp_dolosa'])
    array_morte = np.array(df_total_lesoes_cut['lesao_corp_morte'])

    correlacao = np.corrcoef(array_dolosa, array_morte)[0,1]

    print(f'Correlação: {correlacao}')

except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()


# Regressão linear Análise Preditiva
try:
    print("Iniciando a regressão linear...")

    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    # Agora usamos dolosa (X) para prever morte (y)
    X_train, X_test, y_train, y_test = train_test_split(
                                            array_dolosa,
                                            array_morte,
                                            test_size=0.2,
                                            random_state=42
                                        )
    
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train.reshape(-1, 1))
    X_test = scaler.transform(X_test.reshape(-1, 1))

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    r2_score = modelo.score(X_test, y_test)
    print('R² Score:', r2_score)

    array_lesao_dolosa_pred = np.array([10000, 16000, 21000])
    array_lesao_dolosa_pred_scaled = scaler.transform(array_lesao_dolosa_pred.reshape(-1, 1))

    lesao_morte_pred = modelo.predict(array_lesao_dolosa_pred_scaled)
    print('Previsão de lesões com morte (próximos 3 meses): ', lesao_morte_pred)

except Exception as e:
    print("Erro ao realizar a regressão linear: ", e)
    exit()


# avaliação do modelo
try:
    print('Avaliando o modelo de previsões...')

    plt.subplots(2, 2, figsize=(15, 5))
    plt.suptitle('Avaliação do modelo de regressão')

    plt.subplot(2, 2, 1)
    sns.regplot(x=array_dolosa, y=array_morte)
    plt.title('Gráfico de dispersão')
    plt.xlabel('Lesão dolosa')
    plt.ylabel('Lesão com morte')

    plt.text(min(array_dolosa),
             max(array_morte),
             f'Correlação: {correlacao}',
             fontsize=10)

    plt.subplot(2, 2, 2)
    y_pred = modelo.predict(X_test)
    X_test = scaler.inverse_transform(X_test)

    plt.scatter(X_test, y_test, color='blue', label='Dados reais')
    plt.scatter(X_test, y_pred, color = 'red', label='Previsões')

    plt.title('Dados reais x previstos')
    plt.xlabel('Lesões dolosas')
    plt.ylabel('Lesões com morte')

    plt.legend()

    plt.subplot(2, 2, 3)
    residuos = y_test - y_pred
    plt.scatter(y_pred, residuos)
    plt.axhline(y=0, color='black', linewidth=2)
    plt.title('Resíduos')
    plt.xlabel('Previsões')
    plt.ylabel('Resíduos')

    plt.subplot(2, 2, 4)
    plt.scatter(array_lesao_dolosa_pred, lesao_morte_pred)
    plt.title('Lesões Corporais')
    plt.xlabel('Lesões dolosas simuladas')
    plt.ylabel('Lesões com morte previstas')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Erro ao avaliar o modelo: ", e)
    exit()
